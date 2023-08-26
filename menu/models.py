from django.db import models

# Create your models here.

class FoodCategory(models.Model):
    name=models.CharField(max_length=55,unique=True)

    class Meta:
        verbose_name = 'Food Category'
        verbose_name_plural = 'Food Category'


    def __str__(self):
        return self.name

class DrinkCategory(models.Model):
    name=models.CharField(max_length=55,unique=True)

    class Meta:
        verbose_name = 'Drink Category'
        verbose_name_plural = 'Drink Category'

    def __str__(self):
        return self.name


class BakeryCategory(models.Model):
    name=models.CharField(max_length=55,unique=True)

    class Meta:
        verbose_name = 'Bakery Category'
        verbose_name_plural = 'Bakery Category'

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
    category=models.ForeignKey(BakeryCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Bakery'
        verbose_name_plural = 'Bakery'


    def __str__(self):
        return self.name

class Drink(MenuItem):
    image=models.ImageField(upload_to='images/drinks')
    category=models.ForeignKey(DrinkCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Drink'
        verbose_name_plural = 'Drink'

    def __str__(self):
        return self.name

class Food(MenuItem):
    image=models.ImageField(upload_to='images/foods/')
    category=models.ForeignKey(FoodCategory, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Food'

    def __str__(self):
        return self.name


class Hukka(MenuItem):
    image=models.ImageField(upload_to='images/hukka/')
    class Meta:
        verbose_name = 'Hukka'
        verbose_name_plural = 'Hukka'

    def __str__(self):
        return self.name
