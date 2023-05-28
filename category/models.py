from django.db import models
from django.utils.text import slugify


# Create your models here.
class FoodCategory(models.Model):
    name=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name

class DrinkCategory(models.Model):
    name=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name

class HukkaCategory(models.Model):
    name=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name

class BeakeryCategory(models.Model):
    name=models.CharField(max_length=10,unique=True)

    def __str__(self):
        return self.name
    
    
    