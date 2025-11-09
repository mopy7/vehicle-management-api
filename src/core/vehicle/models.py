from django.db import models

# Create your models here.
class Car(models.Model):
  brand = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  year = models.PositiveSmallIntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)
  
  class Meta:
    verbose_name_plural = "Cars"
    ordering = ['-created_date']

  def __str__(self):
    return f"{self.brand} {self.model} {self.year}"

class Bike(models.Model):
  brand = models.CharField(max_length=50)
  model = models.CharField(max_length=50)
  color = models.CharField(max_length=50)
  year = models.PositiveSmallIntegerField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  created_date = models.DateTimeField(auto_now_add=True)
  updated_date = models.DateTimeField(auto_now=True)

  class Meta:
    verbose_name_plural = "Bikes"
    ordering = ['-created_date']

  def __str__(self):
    return self.model
  