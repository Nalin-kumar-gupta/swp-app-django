from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

class Command(BaseCommand):
    help = 'Flush the database, populate inventory, and create a superuser'

    def handle(self, *args, **options):
        # Hardcoded superuser credentials
        username = 'SrArchitect@walmart'
        email = 'admin@example.com'
        password = 'adminpassword'

        # Flush the database
        self.stdout.write(self.style.WARNING('Flushing the database...'))
        call_command('flush', '--no-input')
        self.stdout.write(self.style.SUCCESS('Database flushed.'))

        # Populate the inventory
        self.stdout.write(self.style.WARNING('Populating inventory...'))
        call_command('populate_inventory')
        self.stdout.write(self.style.SUCCESS('Inventory populated.'))

        # Create superuser
        self.stdout.write(self.style.WARNING('Creating superuser...'))
        User = get_user_model()
        try:
            User.objects.get(username=username)
            self.stdout.write(self.style.ERROR(f'Superuser with username "{username}" already exists.'))
        except ObjectDoesNotExist:
            User.objects.create_superuser(username=username, email=email, password=password)
            self.stdout.write(self.style.SUCCESS('Superuser created.'))
