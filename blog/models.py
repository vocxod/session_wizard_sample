from django.db import models
from django.utils import timezone

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class City(models.Model):
    city_name = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

class Street(models.Model):
    street_name = models.CharField(max_length=250)
    country = models.ForeignKey(City, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    


class Home(models.Model):
    home_name = models.CharField(max_length=250)
    street = models.ForeignKey(Street, on_delete=models.CASCADE)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)    


