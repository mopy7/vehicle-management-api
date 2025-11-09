from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CarSerializer, BikeSerializer
from vehicle.models import Car, Bike
from django.shortcuts import get_object_or_404

class CarListCreateAPIView(APIView):
  def get(self, request):
    cars = Car.objects.all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = CarSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BikeListCreateAPIView(APIView):
  def get(self, request):
    bikes = Bike.objects.all()
    serializer = BikeSerializer(bikes, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def post(self, request):
    serializer = BikeSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class CarDetailAPIView(APIView):
  def get_object(self, pk):
    return get_object_or_404(Car, pk=pk)
  
  def get(self, request, pk):
    car = self.get_object(pk)
    serializer = CarSerializer(car)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk):
    car = self.get_object(pk)
    serializer = CarSerializer(car, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):
    car = self.get_object(pk)
    serializer = CarSerializer(car, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    car = self.get_object(pk)
    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
class BikeDetailAPIView(APIView):
  def get_object(self, pk):
    return get_object_or_404(Bike, pk=pk)
  
  def get(self, request, pk):
    bike = self.get_object(pk)
    serializer = BikeSerializer(bike)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  def put(self, request, pk):
    bike = self.get_object(pk)
    serializer = BikeSerializer(bike, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def patch(self, request, pk):
    bike = self.get_object(pk)
    serializer = BikeSerializer(bike, data=request.data, partial=True)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    bike = self.get_object(pk)
    bike.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)