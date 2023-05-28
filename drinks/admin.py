from django.contrib import admin
from drinks.models import Drink

# Register your models here.

class DrinkAdmin(admin.ModelAdmin):
    list_display=['name','price','category','image','description']

admin.site.register(Drink,DrinkAdmin)