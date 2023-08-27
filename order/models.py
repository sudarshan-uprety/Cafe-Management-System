from django.db import models
from users.models import User
from menu.models import MenuItem, Beakery, Food, Drink, Hukka
# Create your models here.
class Table(models.Model):
    table_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.table_name



class Order(models.Model):
    table_number = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    order_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    food = models.ManyToManyField(Food, blank=True, through="FoodQuantity")
    drink = models.ManyToManyField(Drink, blank=True, through="DrinksQuantity")
    hukka = models.ManyToManyField(Hukka, blank=True, through="HukkaQuantity")
    bakery = models.ManyToManyField(Beakery, blank=True, through="BakeryQuantity")
    order_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.order_by.email
    

class FoodQuantity(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    name = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name.name

class DrinksQuantity(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    name = models.ForeignKey(Drink, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)

class BakeryQuantity(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    name = models.ForeignKey(Beakery, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)

class HukkaQuantity(models.Model):
    quantity = models.PositiveIntegerField(default=1)
    name = models.ForeignKey(Hukka, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
