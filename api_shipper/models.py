from django.db import models

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid



class Package(models.Model):
    # Unique identifier for each box using UUID
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Dimensions of the box in meters
    length = models.IntegerField()
    breadth = models.IntegerField()
    height = models.IntegerField()
    
    # Weight in kilograms
    weight = models.IntegerField()
    
    # Priority of the box (e.g., delivery priority)
    priority = models.IntegerField()

    @property
    def volume(self):
        return self.length * self.breadth * self.height


    def __str__(self):
        return f"Package {self.id} - Volume: {self.volume} m³"



class Trailer(models.Model):
    # Unique identifier for each truck
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    # Dimensions of the truck in meters
    length = models.IntegerField()
    breadth = models.IntegerField()
    height = models.IntegerField()
    
    # Weight metrics in kilograms
    tare_weight = models.IntegerField()
    gvwr = models.IntegerField()  # Gross Vehicle Weight Rating
    
    # Axle weight ratings in kilograms
    axle_weight_ratings = models.JSONField()  # Example: [4000, 4000]
    axle_group_weight_ratings = models.JSONField()  # Example: [6000]

    wheel_load_capacity = models.DecimalField(max_digits=7, decimal_places=2)
    
    # Truck status and additional information
    occupied = models.JSONField(default=list)  # e.g., [True, False, True]
    current_weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    center_of_gravity = models.JSONField(default=[0, 0, 0])  # Example: [x, y, z]

    @property
    def cargo_capacity(self):
        return self.gvwr - self.current_weight
    
    @property
    def space(self):
        # This might be better represented using actual spatial management or more complex structures
        return {'length': self.length, 'breadth': self.breadth, 'height': self.height}
    
    @property
    def weight_distribution(self):
        # Assuming weight distribution involves more than a simple zero matrix, this is an example
        return {'length': self.length, 'breadth': self.breadth, 'height': self.height}

    @property
    def axle_loads(self):
        return [0] * len(self.axle_weight_ratings)

    
    def __str__(self):
        return f"Trailer {self.id} - GVWR: {self.gvwr} kg"