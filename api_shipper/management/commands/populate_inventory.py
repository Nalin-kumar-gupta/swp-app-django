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
            'length': 12.00,
            'breadth': 2.50,
            'height': 4.00,
            'tare_weight': 8000.00,
            'gvwr': 18000.00,
            'axle_weight_ratings': [4000.00, 4000.00, 4000.00],
            'axle_group_weight_ratings': [6000.00, 6000.00],
            'wheel_load_capacity': 5000.00,
            'destination': 'New York'
        }
        
        truck, created = Truck.objects.get_or_create(**truck_data)
        if created:
            self.stdout.write(self.style.SUCCESS(f'Truck created: {truck}'))
        else:
            self.stdout.write(self.style.SUCCESS(f'Truck already exists: {truck}'))
        
        # Create Packages
        packages_data = [
            {'name': 'Electronics Set', 'length': 2.00, 'breadth': 2.00, 'height': 2.00, 'weight': 500.00, 'destination': 'New York', 'deliver_date': date.today() + timedelta(days=1)},
            {'name': 'Books Collection', 'length': 1.50, 'breadth': 1.50, 'height': 1.50, 'weight': 300.00, 'destination': 'Los Angeles', 'deliver_date': date.today() + timedelta(days=2)},
            {'name': 'Furniture Set', 'length': 3.00, 'breadth': 3.00, 'height': 3.00, 'weight': 800.00, 'destination': 'Chicago', 'deliver_date': date.today() + timedelta(days=3)},
            {'name': 'Clothing Box', 'length': 2.50, 'breadth': 2.50, 'height': 2.50, 'weight': 600.00, 'destination': 'Houston', 'deliver_date': date.today() + timedelta(days=4)},
            {'name': 'Kitchen Appliances', 'length': 1.75, 'breadth': 1.75, 'height': 1.75, 'weight': 350.00, 'destination': 'Phoenix', 'deliver_date': date.today() + timedelta(days=5)},
            {'name': 'Fitness Equipment', 'length': 2.00, 'breadth': 2.00, 'height': 2.00, 'weight': 500.00, 'destination': 'Philadelphia', 'deliver_date': date.today() + timedelta(days=6)},
            {'name': 'Office Supplies', 'length': 1.50, 'breadth': 1.50, 'height': 1.50, 'weight': 300.00, 'destination': 'San Antonio', 'deliver_date': date.today() + timedelta(days=7)},
            {'name': 'Home Decor', 'length': 3.00, 'breadth': 3.00, 'height': 3.00, 'weight': 800.00, 'destination': 'San Diego', 'deliver_date': date.today() + timedelta(days=8)},
            {'name': 'Sports Gear', 'length': 2.50, 'breadth': 2.50, 'height': 2.50, 'weight': 600.00, 'destination': 'Dallas', 'deliver_date': date.today() + timedelta(days=9)},
            {'name': 'Medical Supplies', 'length': 1.75, 'breadth': 1.75, 'height': 1.75, 'weight': 350.00, 'destination': 'San Jose', 'deliver_date': date.today() + timedelta(days=10)},
            {'name': 'Toys and Games', 'length': 2.00, 'breadth': 2.00, 'height': 2.00, 'weight': 500.00, 'destination': 'Austin', 'deliver_date': date.today() + timedelta(days=11)},
            {'name': 'Camping Gear', 'length': 1.50, 'breadth': 1.50, 'height': 1.50, 'weight': 300.00, 'destination': 'Jacksonville', 'deliver_date': date.today() + timedelta(days=12)},
            {'name': 'Pet Supplies', 'length': 3.00, 'breadth': 3.00, 'height': 3.00, 'weight': 800.00, 'destination': 'Columbus', 'deliver_date': date.today() + timedelta(days=13)},
            {'name': 'Garden Tools', 'length': 2.50, 'breadth': 2.50, 'height': 2.50, 'weight': 600.00, 'destination': 'Indianapolis', 'deliver_date': date.today() + timedelta(days=14)},
            {'name': 'Beauty Products', 'length': 1.75, 'breadth': 1.75, 'height': 1.75, 'weight': 350.00, 'destination': 'San Francisco', 'deliver_date': date.today() + timedelta(days=15)},
            {'name': 'Books and Magazines', 'length': 2.00, 'breadth': 2.00, 'height': 2.00, 'weight': 500.00, 'destination': 'Seattle', 'deliver_date': date.today() + timedelta(days=16)},
        ]
        
        for package_data in packages_data:
            package = Package.objects.create(**package_data)
            self.stdout.write(self.style.SUCCESS(f'Package created: {package}'))
