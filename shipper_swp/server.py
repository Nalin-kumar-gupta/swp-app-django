import numpy as np
import plotly.graph_objects as go
import http.server
import socketserver
from flask import Flask, request, jsonify, render_template, abort
import plotly.graph_objects as go
import numpy as np

app = Flask(__name__)


class Box:
    def __init__(self, id, length, breadth, height, weight, priority, box_id):
        self.id = id
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
    def __init__(self, id, model_name, length, breadth, height, tare_weight, gvwr, axle_weight_ratings, axle_group_weight_ratings, wheel_load_capacity):
        self.id = id
        self.model_name = model_name
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
        self.center_of_gravity = [length / 2, breadth / 2, height / 2]
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
            self.center_of_gravity = [self.length / 2, self.breadth / 2, self.height / 2]
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

    axle_colors = ['blue', 'green', 'red', 'cyan']
    highlighted_box_id = None

    # Plot boxes
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
            color=color,
            name=box.box_id
        ))

    # Plot axles
    for i, position in enumerate(np.linspace(0, truck.length, len(truck.axle_weight_ratings))):
        fig.add_trace(go.Scatter3d(
            x=[position, position],
            y=[0, truck.breadth],
            z=[0, 0],
            mode='lines+text',
            line=dict(color='black', width=4),
            text=[f'Axle {i+1}', f'Load: {truck.axle_loads[i]:.2f} kg'],
            textposition='top right',
            name=f'Axle {i+1}'
        ))

    # Add scatter plot for box IDs
    ids_x = [x + box.length / 2 for box, x, y, z in occupied_boxes]
    ids_y = [y + box.breadth / 2 for box, x, y, z in occupied_boxes]
    ids_z = [z + box.height / 2 for box, x, y, z in occupied_boxes]
    ids_text = [box.box_id for box, x, y, z in occupied_boxes]
    
    fig.add_trace(go.Scatter3d(
        x=ids_x,
        y=ids_y,
        z=ids_z,
        mode='text',
        text=ids_text,
        textposition='middle center',
        marker=dict(size=5, color='black'),
        name='Box IDs'
    ))

    # Calculate and annotate center of gravity and total weight
    cog_x, cog_y, cog_z = truck.center_of_gravity
    total_weight = truck.current_weight + truck.tare_weight

    # Add center of mass trace
    fig.add_trace(go.Scatter3d(
        x=[cog_x],
        y=[cog_y],
        z=[cog_z],
        mode='markers+text',
        marker=dict(size=10, color='red'),
        text=['Center of Gravity'],
        textposition='top center',
        name='Center of Gravity'
    ))

    # Add total weight annotation as text
    fig.add_trace(go.Scatter3d(
        x=[truck.length / 2],
        y=[truck.breadth / 2],
        z=[-truck.height * 0.1],  # Position this annotation below the plot
        mode='text',
        text=[f"Total Weight: {total_weight:.2f} kg"],
        textposition='bottom center',
        name='Total Weight'
    ))

    fig.update_layout(
        scene=dict(
            xaxis_title='X',
            yaxis_title='Y',
            zaxis_title='Z',
            xaxis=dict(
                nticks=10,
                range=[0, truck.length],
                title='Length'
            ),
            yaxis=dict(
                nticks=10,
                range=[0, truck.breadth],
                title='Breadth'
            ),
            zaxis=dict(
                nticks=10,
                range=[0, truck.height],
                title='Height'
            ),
            aspectratio=dict(
                x=truck.length / max(truck.breadth, truck.height),
                y=truck.breadth / max(truck.length, truck.height),
                z=truck.height / max(truck.length, truck.breadth)
            )
        ),
        title='3D Visualization of Packed Boxes'
    )

    fig.update_layout(
        updatemenus=[
            dict(
                type="dropdown",
                x=1.15,
                y=0.8,
                buttons=[
                    dict(
                        label="Highlight",
                        method="update",
                        args=[{"showlegend": True}]
                    ),
                    dict(
                        label="Reset",
                        method="update",
                        args=[{"showlegend": True}]
                    )
                ]
            )
        ]
    )
    
    fig.write_html(f"shipper_swp/templates/truck_visualization_{truck.id}.html")


@app.route('/process/', methods=['POST'])
def process():
    data = request.get_json()
    boxes = [Box(**box_data) for box_data in data['boxes']]
    truck = Truck(**data['truck'])
    pack_boxes(boxes, truck)
    plotly_draw_boxes(truck, truck.occupied)
    return jsonify({'message': 'Boxes packed and visualization generated'})

@app.route('/visualization/<string:truck_id>/', methods=['GET'])
def visualization(truck_id):
    # Construct the template name based on the truck_id
    template_name = f'truck_visualization_{truck_id}.html'

    try:
        # Attempt to render the requested template
        return render_template(template_name)
    except Exception:
        # Render a warning page if the specific template does not exist
        return render_template('warning.html', message="The visualization does not exist or the URL might be incorrect"), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)