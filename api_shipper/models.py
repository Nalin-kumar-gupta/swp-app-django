from django.db import models
from django.contrib.auth.models import User
import uuid



class Truck(models.Model):
    # Unique identifier for each truck
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    model_name = models.CharField(max_length=20, unique=True) 
    
    # Dimensions of the truck in meters
    length = models.DecimalField(max_digits=6, decimal_places=2)
    breadth = models.DecimalField(max_digits=6, decimal_places=2)
    height = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Weight metrics in kilograms
    tare_weight = models.DecimalField(max_digits=10, decimal_places=2)
    gvwr = models.DecimalField(max_digits=10, decimal_places=2)  # Gross Vehicle Weight Rating
    
    # Axle weight ratings in kilograms (JSONField for flexibility)
    axle_weight_ratings = models.JSONField()  # Example: [4000.0, 4000.0]
    axle_group_weight_ratings = models.JSONField()  # Example: [6000.0]

    wheel_load_capacity = models.DecimalField(max_digits=10, decimal_places=2)

    STATUS_CHOICES = [
        ('entered', 'Entered the Inventory'),
        ('loaded', 'Allocated Packages'),
        ('dispatched', 'Dispatched')
    ]
    destination = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inventory', editable=False)

    def save(self, *args, **kwargs):
        if self.destination:
            self.destination = self.destination.upper()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Truck {self.id} - GVWR: {self.gvwr} kg"
    
class Package(models.Model):
    # Unique identifier for each package using UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=20, unique=True) 
    # Dimensions of the package in meters (using DecimalField for more precision)
    length = models.DecimalField(max_digits=5, decimal_places=2)
    breadth = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    
    # Weight in kilograms (using DecimalField for precision)
    weight = models.DecimalField(max_digits=6, decimal_places=2)
    
    # Status of the package
    STATUS_CHOICES = [
        ('inventory', 'Inventory'),
        ('allocated', 'Allocated to Truck'),
        ('dispatched', 'Dispatched')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='inventory', editable=False)
    destination = models.CharField(max_length=50)
    deliver_date = models.DateField()

    allocation = models.CharField(max_length=50, default="---")

    @property
    def volume(self):
        return self.length * self.breadth * self.height
    
    @property
    def priority(self):
        # TODO
        return ""


    def save(self, *args, **kwargs):
        if self.destination:
            self.destination = self.destination.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Package {self.id} - Volume: {self.volume} m³"


