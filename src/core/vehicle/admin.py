from django.contrib import admin
from .models import Car, Bike

# Register your models here.
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'price', 'created_date')
    search_fields = ('brand', 'model', 'color')
    list_filter = ('brand', 'year', 'color')

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'color', 'price', 'created_date')
    search_fields = ('brand', 'model', 'color')
    list_filter = ('brand', 'year', 'color')
