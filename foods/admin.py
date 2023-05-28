from django.contrib import admin
from foods.models import Food

# Register your models here.

class FoodAdmin(admin.ModelAdmin):
    list_display=['name','price','category','image','description']


admin.site.register(Food,FoodAdmin)