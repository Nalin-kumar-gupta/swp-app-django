from django.core.management.base import BaseCommand
from api_shipper.models import Trailer, Package

class Command(BaseCommand):
    help = 'Populate the database with hardcoded Truck and Box data'

    def handle(self, *args, **kwargs):
        # Create Truck
        truck_data = {
            'length': 10,
            'breadth': 5,
            'height': 5,
            'tare_weight': 1000,
            'gvwr': 8000,
            'axle_weight_ratings': [4000, 4000],
            'axle_group_weight_ratings': [6000],
            'wheel_load_capacity': 2000,
        }
        
        truck, created = Trailer.objects.get_or_create(**truck_data)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Truck created: {truck}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Truck already exists: {truck}'))
        
        # Create Boxes
        boxes_data = [
            {'length': 2, 'breadth': 2, 'height': 2, 'weight': 500, 'priority': 1},
            {'length': 1, 'breadth': 1, 'height': 1, 'weight': 100, 'priority': 3},
            {'length': 3, 'breadth': 3, 'height': 3, 'weight': 900, 'priority': 2},
            {'length': 1, 'breadth': 2, 'height': 1, 'weight': 200, 'priority': 4},
            {'length': 2, 'breadth': 2, 'height': 2, 'weight': 500, 'priority': 1},
            {'length': 1, 'breadth': 1, 'height': 1, 'weight': 100, 'priority': 3},
            {'length': 3, 'breadth': 3, 'height': 3, 'weight': 900, 'priority': 2},
            {'length': 1, 'breadth': 2, 'height': 1, 'weight': 200, 'priority': 4},
            {'length': 2, 'breadth': 2, 'height': 2, 'weight': 500, 'priority': 1},
            {'length': 1, 'breadth': 1, 'height': 1, 'weight': 100, 'priority': 3},
            {'length': 1, 'breadth': 1, 'height': 1, 'weight': 100, 'priority': 3},
            {'length': 1, 'breadth': 1, 'height': 1, 'weight': 100, 'priority': 3},
            {'length': 1, 'breadth': 1, 'height': 1, 'weight': 100, 'priority': 3},
            {'length': 1, 'breadth': 1, 'height': 1, 'weight': 200, 'priority': 3},
            {'length': 2, 'breadth': 1, 'height': 1, 'weight': 200, 'priority': 3}
        ]
        
        for box_data in boxes_data:
            box = Package.objects.create(**box_data)
            self.stdout.write(self.style.SUCCESS(f'Box created: {box}'))

