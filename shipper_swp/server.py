import numpy as np
import plotly.graph_objects as go
import http.server
import socketserver

class Box:
    def __init__(self, length, breadth, height, weight, priority, box_id):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.weight = weight
        self.priority = priority
        self.box_id = box_id
        self.volume = length * breadth * height

    def get_rotations(self):
        return [
            Box(self.length, self.breadth, self.height, self.weight, self.priority, self.box_id),
            Box(self.length, self.height, self.breadth, self.weight, self.priority, self.box_id),
            Box(self.breadth, self.length, self.height, self.weight, self.priority, self.box_id),
            Box(self.breadth, self.height, self.length, self.weight, self.priority, self.box_id),
            Box(self.height, self.length, self.breadth, self.weight, self.priority, self.box_id),
            Box(self.height, self.breadth, self.length, self.weight, self.priority, self.box_id)
        ]

class Truck:
    def __init__(self, length, breadth, height, tare_weight, gvwr, axle_weight_ratings, axle_group_weight_ratings, wheel_load_capacity):
        self.length = length
        self.breadth = breadth
        self.height = height
        self.tare_weight = tare_weight
        self.gvwr = gvwr
        self.cargo_capacity = gvwr - tare_weight
        self.axle_weight_ratings = axle_weight_ratings
        self.axle_group_weight_ratings = axle_group_weight_ratings
        self.wheel_load_capacity = wheel_load_capacity
        self.space = np.zeros((length, breadth, height), dtype=bool)
        self.weight_distribution = np.zeros((length, breadth, height), dtype=float)
        self.occupied = []
        self.current_weight = 0
        self.center_of_gravity = [0, 0, 0]
        self.axle_loads = [0] * len(axle_weight_ratings)

    def can_place_box(self, box, x, y, z):
        if x + box.length > self.length or y + box.breadth > self.breadth or z + box.height > self.height:
            return False
        for i in range(box.length):
            for j in range(box.breadth):
                for k in range(box.height):
                    if self.space[x+i, y+j, z+k]:
                        return False
        return True

    def place_box(self, box, x, y, z):
        for i in range(box.length):
            for j in range(box.breadth):
                for k in range(box.height):
                    self.space[x+i, y+j, z+k] = True
                    self.weight_distribution[x+i, y+j, z+k] += box.weight / (box.length * box.breadth * box.height)
        self.occupied.append((box, x, y, z))
        self.current_weight += box.weight
        self.update_center_of_gravity(box, x, y, z)
        self.update_axle_loads(box, x)

    def remove_box(self, box, x, y, z):
        for i in range(box.length):
            for j in range(box.breadth):
                for k in range(box.height):
                    self.space[x+i, y+j, z+k] = False
                    self.weight_distribution[x+i, y+j, z+k] -= box.weight / (box.length * box.breadth * box.height)
        self.occupied.remove((box, x, y, z))
        self.current_weight -= box.weight
        self.update_center_of_gravity_after_removal(box, x, y, z)
        self.update_axle_loads_after_removal(box, x)

    def update_center_of_gravity(self, box, x, y, z):
        total_mass = self.current_weight + self.tare_weight
        new_cog_x = (self.center_of_gravity[0] * (total_mass - box.weight) + (x + box.length / 2) * box.weight) / total_mass
        new_cog_y = (self.center_of_gravity[1] * (total_mass - box.weight) + (y + box.breadth / 2) * box.weight) / total_mass
        new_cog_z = (self.center_of_gravity[2] * (total_mass - box.weight) + (z + box.height / 2) * box.weight) / total_mass
        self.center_of_gravity = [new_cog_x, new_cog_y, new_cog_z]

    def update_center_of_gravity_after_removal(self, box, x, y, z):
        total_mass = self.current_weight + self.tare_weight
        if total_mass == 0:
            self.center_of_gravity = [0, 0, 0]
        else:
            new_cog_x = (self.center_of_gravity[0] * (total_mass + box.weight) - (x + box.length / 2) * box.weight) / total_mass
            new_cog_y = (self.center_of_gravity[1] * (total_mass + box.weight) - (y + box.breadth / 2) * box.weight) / total_mass
            new_cog_z = (self.center_of_gravity[2] * (total_mass + box.weight) - (z + box.height / 2) * box.weight) / total_mass
            self.center_of_gravity = [new_cog_x, new_cog_y, new_cog_z]

    def update_axle_loads(self, box, x):
        axle_index = int(x / (self.length / len(self.axle_weight_ratings)))
        self.axle_loads[axle_index] += box.weight

    def update_axle_loads_after_removal(self, box, x):
        axle_index = int(x / (self.length / len(self.axle_weight_ratings)))
        self.axle_loads[axle_index] -= box.weight

    def check_axle_loads(self):
        for i, load in enumerate(self.axle_loads):
            if load > self.axle_weight_ratings[i]:
                return False
        return True

def find_best_position(truck, box):
    best_position = None
    best_volume_left = -1
    
    for z in range(truck.height - box.height + 1):
        for y in range(truck.breadth - box.breadth + 1):
            for x in range(truck.length - box.length + 1):
                if truck.can_place_box(box, x, y, z):
                    volume_left = (truck.length - x - box.length) * (truck.breadth - y - box.breadth)
                    if volume_left > best_volume_left:
                        best_volume_left = volume_left
                        best_position = (x, y, z)
    return best_position

def pack_boxes(boxes, truck):
    sorted_boxes = sorted(boxes, key=lambda box: (-box.priority, -box.volume))
    
    for z in range(truck.height):
        for y in range(truck.breadth):
            for x in range(truck.length):
                for box in sorted_boxes:
                    if truck.can_place_box(box, x, y, z):
                        truck.place_box(box, x, y, z)
                        if not truck.check_axle_loads():
                            truck.remove_box(box, x, y, z)
                        else:
                            sorted_boxes.remove(box)
                            break  # Move to the next position after placing a box
    return truck.occupied


def calculate_volume_left(box, x, y, z, truck):
    volume_left = 0
    for i in range(x, min(x + box.length, truck.length)):
        for j in range(y, min(y + box.breadth, truck.breadth)):
            for k in range(z, min(z + box.height, truck.height)):
                if not truck.space[i, j, k]:
                    volume_left += 1
    return volume_left


def plotly_draw_boxes(truck, occupied_boxes):
    fig = go.Figure()

    axle_colors = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow']
    for idx, (box, x, y, z) in enumerate(occupied_boxes):
        axle_index = int(x / (truck.length / len(truck.axle_weight_ratings)))
        color = axle_colors[axle_index % len(axle_colors)]

        # Define vertices for the box
        vertices = {
            'x': [x, x + box.length, x + box.length, x, x, x + box.length, x + box.length, x],
            'y': [y, y, y + box.breadth, y + box.breadth, y, y, y + box.breadth, y + box.breadth],
            'z': [z, z, z, z, z + box.height, z + box.height, z + box.height, z + box.height]
        }
        
        faces = [
            [0, 1, 5, 4],
            [1, 2, 6, 5],
            [2, 3, 7, 6],
            [3, 0, 4, 7],
            [0, 1, 2, 3],
            [4, 5, 6, 7]
        ]
        
        i, j, k = [], [], []
        for face in faces:
            i.append(face[0])
            j.append(face[1])
            k.append(face[2])
            i.append(face[0])
            j.append(face[2])
            k.append(face[3])

        fig.add_trace(go.Mesh3d(
            x=vertices['x'],
            y=vertices['y'],
            z=vertices['z'],
            i=i,
            j=j,
            k=k,
            opacity=0.5,
            color=color
        ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            xaxis=dict(nticks=4, range=[0, truck.length]),
            yaxis=dict(nticks=4, range=[0, truck.breadth]),
            zaxis=dict(nticks=4, range=[0, truck.height]),
            aspectratio=dict(x=1, y=1, z=1)  # Ensures equal scaling for all axes
        ),
        title='3D Visualization of Packed Boxes'
    )

    fig.write_html("shipper_swp/templates/truck_visualization_plotly.html")


# Example usage
# Example usage
boxes = [
    Box(2, 2, 2, 500, 1, "Box1"),
    Box(1, 1, 1, 100, 3, "Box2"),
    Box(3, 3, 3, 900, 2, "Box3"),
    Box(1, 2, 1, 200, 4, "Box4"),
    Box(2, 2, 2, 500, 1, "Box5"),
    Box(1, 1, 1, 100, 3, "Box6"),
    Box(3, 3, 3, 900, 2, "Box7"),
    Box(1, 2, 1, 200, 4, "Box8"),
    Box(2, 2, 2, 500, 1, "Box9"),
    Box(1, 1, 1, 100, 3, "Box10"),
    Box(1, 1, 1, 100, 3, "Box11"),
    Box(1, 1, 1, 100, 3, "Box12"),
    Box(1, 1, 1, 100, 3, "Box13"),
    Box(1, 1, 1, 200, 3, "Box14"),
    Box(2, 1, 1, 200, 3, "Box15"),
    Box(2, 2, 2, 500, 1, "Box1"),
]

truck = Truck(length=5, breadth=5, height=6, tare_weight=2000, gvwr=10000, axle_weight_ratings=[2000, 2000, 2000, 2000], axle_group_weight_ratings=[8000], wheel_load_capacity=5000)

pack_boxes(boxes, truck)
plotly_draw_boxes(truck, truck.occupied)

# Set up the HTTP server
PORT = 8080
class Handler(http.server.SimpleHTTPRequestHandler):
    pass

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()
