from rest_framework import serializers
from vehicle.models import Car, Bike

class CarSerializer(serializers.ModelSerializer):
  class Meta:
    model = Car
    fields = '__all__'

class BikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bike
    fields = '__all__'