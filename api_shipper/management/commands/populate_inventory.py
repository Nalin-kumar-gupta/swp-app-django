from django.core.management.base import BaseCommand
from api_shipper.models import Truck, Package
import uuid
from datetime import date, timedelta

class Command(BaseCommand):
    help = 'Populate the database with hardcoded Truck and Package data'

    def handle(self, *args, **kwargs):
        # Create Truck
        truck_data = {
            'model_name': 'Volvo FH16',
            'length': 10.00,
            'breadth': 6.00,
            'height': 6.00,
            'tare_weight': 5000.00,
            'gvwr': 15000.00,
            'axle_weight_ratings': [5000.00, 5000.00, 5000.00],
            'axle_group_weight_ratings': [10000.00, 10000.00],
            'wheel_load_capacity': 500.00,
            'destination': 'New York'
        }
        
        truck, created = Truck.objects.get_or_create(**truck_data)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Truck created: {truck}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Truck already exists: {truck}'))
        
        # Create Packages
        packages_data = [
            {'name': 'Electronics Set', 'length': 3.00, 'breadth': 4.00, 'height': 2.00, 'weight': 500.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=1), 'stock': 4},
            {'name': 'Books Collection', 'length': 4.50, 'breadth': 2.50, 'height': 1.30, 'weight': 300.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=2), 'stock': 4},
            {'name': 'Furniture Set', 'length': 2.00, 'breadth': 2.00, 'height': 2.00, 'weight': 800.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=3), 'stock': 6}, #4
            {'name': 'Clothing Box', 'length': 1.50, 'breadth': 3.50, 'height': 2.50, 'weight': 600.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=4), 'stock': 4},
            {'name': 'Kitchen Appliances', 'length': 3.35, 'breadth': 4.15, 'height': 2.05, 'weight': 350.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=5), 'stock': 6}, #4
            {'name': 'Fitness Equipment', 'length': 4.00, 'breadth': 2.00, 'height': 1.00, 'weight': 500.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=6), 'stock': 4},
            {'name': 'Office Supplies', 'length': 2.00, 'breadth': 2.00, 'height': 2.00, 'weight': 300.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=7), 'stock': 4},
            {'name': 'Home Decor', 'length': 1.00, 'breadth': 3.00, 'height': 2.00, 'weight': 800.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=8), 'stock': 4},
            {'name': 'Sports Gear', 'length': 2.50, 'breadth': 2.50, 'height': 2.50, 'weight': 600.00, 'destination': 'NewYork', 'deliver_date': date.today() + timedelta(days=9), 'stock': 4},
            {'name': 'Medical Supplies', 'length': 3.00, 'breadth': 4.00, 'height': 2.00, 'weight': 350.00, 'destination': 'Jacksonville', 'deliver_date': date.today() + timedelta(days=10), 'stock': 4},
            {'name': 'Toys and Games', 'length': 4.00, 'breadth': 2.00, 'height': 1.00, 'weight': 500.00, 'destination': 'Jacksonville', 'deliver_date': date.today() + timedelta(days=11), 'stock': 6},
            {'name': 'Camping Gear', 'length': 1.00, 'breadth': 4.00, 'height': 1.00, 'weight': 300.00, 'destination': 'San Francisco', 'deliver_date': date.today() + timedelta(days=12), 'stock': 5},
            {'name': 'Pet Supplies', 'length': 1.00, 'breadth': 3.00, 'height': 2.00, 'weight': 800.00, 'destination': 'Columbus', 'deliver_date': date.today() + timedelta(days=13), 'stock': 3},
            {'name': 'Garden Tools', 'length': 2.50, 'breadth': 2.50, 'height': 2.50, 'weight': 600.00, 'destination': 'Miami', 'deliver_date': date.today() + timedelta(days=14), 'stock': 4},
            {'name': 'Beauty Products', 'length': 1.75, 'breadth': 1.75, 'height': 1.75, 'weight': 350.00, 'destination': 'Boston', 'deliver_date': date.today() + timedelta(days=15), 'stock': 6},
            {'name': 'Books and Magazines', 'length': 2.00, 'breadth': 2.00, 'height': 2.00, 'weight': 500.00, 'destination': 'Seattle', 'deliver_date': date.today() + timedelta(days=16), 'stock': 7},
            {'name': 'Musical Instruments', 'length': 3.00, 'breadth': 1.50, 'height': 1.50, 'weight': 450.00, 'destination': 'Houston', 'deliver_date': date.today() + timedelta(days=17), 'stock': 2},
            {'name': 'Laptop Bag', 'length': 1.20, 'breadth': 2.50, 'height': 0.80, 'weight': 200.00, 'destination': 'Denver', 'deliver_date': date.today() + timedelta(days=1), 'stock': 5},
            {'name': 'Smartphone Bundle', 'length': 0.50, 'breadth': 0.75, 'height': 0.25, 'weight': 50.00, 'destination': 'Orlando', 'deliver_date': date.today() + timedelta(days=2), 'stock': 8},
            {'name': 'Gaming Console', 'length': 2.00, 'breadth': 3.00, 'height': 1.50, 'weight': 400.00, 'destination': 'San Diego', 'deliver_date': date.today() + timedelta(days=3), 'stock': 4},
            {'name': 'Smart Home Devices', 'length': 1.75, 'breadth': 2.50, 'height': 1.25, 'weight': 350.00, 'destination': 'Las Vegas', 'deliver_date': date.today() + timedelta(days=4), 'stock': 6},
            {'name': 'Camera Equipment', 'length': 1.50, 'breadth': 2.00, 'height': 1.00, 'weight': 300.00, 'destination': 'San Jose', 'deliver_date': date.today() + timedelta(days=5), 'stock': 3},
            {'name': 'Video Games', 'length': 0.75, 'breadth': 1.25, 'height': 0.30, 'weight': 80.00, 'destination': 'Phoenix', 'deliver_date': date.today() + timedelta(days=6), 'stock': 9},
            {'name': 'Sports Equipment', 'length': 2.50, 'breadth': 3.50, 'height': 2.00, 'weight': 500.00, 'destination': 'Austin', 'deliver_date': date.today() + timedelta(days=7), 'stock': 7},
            {'name': 'Art Supplies', 'length': 1.00, 'breadth': 1.50, 'height': 0.75, 'weight': 120.00, 'destination': 'San Antonio', 'deliver_date': date.today() + timedelta(days=8), 'stock': 4},
            {'name': 'Hardware Tools', 'length': 2.00, 'breadth': 3.00, 'height': 1.50, 'weight': 450.00, 'destination': 'Dallas', 'deliver_date': date.today() + timedelta(days=9), 'stock': 5},
            {'name': 'Outdoor Furniture', 'length': 3.00, 'breadth': 4.00, 'height': 2.00, 'weight': 600.00, 'destination': 'Miami', 'deliver_date': date.today() + timedelta(days=10), 'stock': 3},
            {'name': 'Gardening Supplies', 'length': 2.50, 'breadth': 3.00, 'height': 1.50, 'weight': 400.00, 'destination': 'Seattle', 'deliver_date': date.today() + timedelta(days=11), 'stock': 6},
            {'name': 'Bedding Set', 'length': 2.00, 'breadth': 2.50, 'height': 1.00, 'weight': 300.00, 'destination': 'Boston', 'deliver_date': date.today() + timedelta(days=12), 'stock': 5},
            {'name': 'Jewelry Box', 'length': 0.50, 'breadth': 0.75, 'height': 0.30, 'weight': 50.00, 'destination': 'Atlanta', 'deliver_date': date.today() + timedelta(days=13), 'stock': 10},
            {'name': 'Health Supplements', 'length': 1.25, 'breadth': 2.00, 'height': 1.00, 'weight': 200.00, 'destination': 'Tampa', 'deliver_date': date.today() + timedelta(days=14), 'stock': 8},
            {'name': 'Baby Products', 'length': 2.00, 'breadth': 3.00, 'height': 1.50, 'weight': 350.00, 'destination': 'Portland', 'deliver_date': date.today() + timedelta(days=15), 'stock': 6},
            {'name': 'Toys Set', 'length': 1.00, 'breadth': 2.50, 'height': 1.00, 'weight': 150.00, 'destination': 'Minneapolis', 'deliver_date': date.today() + timedelta(days=16), 'stock': 7},
            {'name': 'Guitar', 'length': 3.00, 'breadth': 1.50, 'height': 1.50, 'weight': 450.00, 'destination': 'Houston', 'deliver_date': date.today() + timedelta(days=17), 'stock': 2},
        ]
        
        for package_data in packages_data:
            package = Package.objects.create(**package_data)
            self.stdout.write(self.style.SUCCESS(f'Package created: {package}'))
