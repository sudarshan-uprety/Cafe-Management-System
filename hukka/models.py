from django.db import models
from category.models import HukkaCategory
# Create your models here.
class Hukka(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category=models.ForeignKey(HukkaCategory, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/hukka/')

    def __str__(self):
        return self.name
    
    # def __str__(self):
    #     return self.price