from django.urls import path
from .views import CarListCreateAPIView, BikeListCreateAPIView, CarDetailAPIView, BikeDetailAPIView

urlpatterns = [
  path("cars/", CarListCreateAPIView.as_view(), name="car-list-create"),
  path("bikes/", BikeListCreateAPIView.as_view(), name="bike-list-create"),
  path("cars/<int:pk>/", CarDetailAPIView.as_view(), name="car-detail"),
  path("bikes/<int:pk>/", BikeDetailAPIView.as_view(), name="bike-detail"),
]