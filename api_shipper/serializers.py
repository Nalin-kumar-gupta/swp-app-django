from rest_framework import serializers
from .models import Package

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['id', 'name', 'length', 'breadth', 'height', 'weight', 'status', 'destination', 'deliver_date', 'allocation', 'volume', 'priority']
        read_only_fields = ['id', 'volume', 'priority']

    def validate(self, data):
        # Example validation, adjust according to your needs
        if data['length'] <= 0 or data['breadth'] <= 0 or data['height'] <= 0:
            raise serializers.ValidationError("Dimensions must be positive values.")
        if data['weight'] <= 0:
            raise serializers.ValidationError("Weight must be a positive value.")
        if data['deliver_date'] < date.today():
            raise serializers.ValidationError("Delivery date cannot be in the past.")
        return data
    

from rest_framework import serializers
from .models import Truck

class TruckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Truck
        fields = ['id', 'model_name', 'length', 'breadth', 'height', 'tare_weight', 'gvwr', 'axle_weight_ratings', 'axle_group_weight_ratings', 'wheel_load_capacity', 'destination', 'status']
        read_only_fields = ['id', 'status']

    def validate(self, data):
        # Validate dimensions
        if data['length'] <= 0 or data['breadth'] <= 0 or data['height'] <= 0:
            raise serializers.ValidationError("Dimensions must be positive values.")
        
        # Validate weights
        if data['tare_weight'] <= 0 or data['gvwr'] <= 0:
            raise serializers.ValidationError("Weight metrics must be positive values.")
        
        # Validate axle weights
        if not all(weight > 0 for weight in data.get('axle_weight_ratings', [])):
            raise serializers.ValidationError("All axle weight ratings must be positive values.")
        
        # Validate wheel load capacity
        if data['wheel_load_capacity'] <= 0:
            raise serializers.ValidationError("Wheel load capacity must be a positive value.")
        
        # Validate destination
        if len(data['destination']) > 50:
            raise serializers.ValidationError("Destination cannot be more than 50 characters long.")
        
        return data
