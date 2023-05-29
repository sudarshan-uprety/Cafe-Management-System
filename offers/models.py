from django.db import models
from foods.models import Food
from drinks.models import Drink
from hukka.models import Hukka
from beakery.models import Beakery

# Create your models here.

class FoodOffers(models.Model):
    name = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='food_offers')
    discount_rate = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    def save(self, *args, **kwargs):
        self.price = self.name.price
        self.offer_price = self.price - (self.price * self.discount_rate / 100)
        super().save(*args, **kwargs)



class DrinkOffers(models.Model):
    name = models.ForeignKey(Drink, on_delete=models.CASCADE, related_name='drink_offers')
    discount_rate = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    def save(self, *args, **kwargs):
        self.price = self.name.price
        self.offer_price = self.price - (self.price * self.discount_rate / 100)
        super().save(*args, **kwargs)


class HukkaOffers(models.Model):
    name = models.ForeignKey(Hukka, on_delete=models.CASCADE, related_name='hukka_offers')
    discount_rate = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    def save(self, *args, **kwargs):
        self.price = self.name.price
        self.offer_price = self.price - (self.price * self.discount_rate / 100)
        super().save(*args, **kwargs)


class BeakeryOffers(models.Model):
    name = models.ForeignKey(Beakery, on_delete=models.CASCADE, related_name='beakery_offers')
    discount_rate = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)

    def save(self, *args, **kwargs):
        self.price = self.name.price
        self.offer_price = self.price - (self.price * self.discount_rate / 100)
        super().save(*args, **kwargs)
