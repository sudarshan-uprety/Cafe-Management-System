from django.db import models
from category.models import FoodCategory
# Create your models here.

class Food(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price=models.CharField(max_length=5)
    category=models.ForeignKey(FoodCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/foods/')