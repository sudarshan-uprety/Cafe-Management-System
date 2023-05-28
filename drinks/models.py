from django.db import models
from category.models import DrinkCategory
# Create your models here.

class Drink(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.CharField(max_length=5)
    category=models.ForeignKey(DrinkCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/drinks')