from django.db import models

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
    
class MenuItem(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.name


class Beakery(MenuItem):
    image=models.ImageField(upload_to='images/beakery')
    category=models.ForeignKey(BeakeryCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Drink(MenuItem):
    image=models.ImageField(upload_to='images/drinks')
    category=models.ForeignKey(DrinkCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Food(MenuItem):
    image=models.ImageField(upload_to='images/foods/')
    category=models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hukka(MenuItem):
    image=models.ImageField(upload_to='images/hukka/')
    category=models.ForeignKey(HukkaCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
