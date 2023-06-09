from django.db import models
from category.models import DrinkCategory
# Create your models here.

class Drink(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(DrinkCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/drinks')

    def __str__(self):
        return self.name
    