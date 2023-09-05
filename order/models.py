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
    food = models.ManyToManyField(Food, blank=True, through="FoodOrder")
    drink = models.ManyToManyField(Drink, blank=True, through="DrinkOrder")
    hukka = models.ManyToManyField(Hukka, blank=True, through="HukkaOrder")
    bakery = models.ManyToManyField(Beakery, blank=True, through="BakeryOrder")
    order_time = models.DateTimeField(auto_now_add=True)
    total_amount = models.FloatField(blank=True, null=True)


    def __str__(self):
        return str(self.table_number)
    

class FoodOrder(models.Model):
    name = models.ForeignKey(Food, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name.name

class DrinkOrder(models.Model):
    name = models.ForeignKey(Drink, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name.name

class BakeryOrder(models.Model):
    name = models.ForeignKey(Beakery, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name.name

class HukkaOrder(models.Model):
    name = models.ForeignKey(Hukka, on_delete=models.CASCADE)
    order = models.ForeignKey("Order", on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.name.name