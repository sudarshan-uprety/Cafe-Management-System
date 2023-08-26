from django.contrib import admin
from menu.models import Drink, Hukka, Beakery, Food, FoodCategory, DrinkCategory, BakeryCategory

# Register your models here.

class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class DrinksCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class BakeryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class DrinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class HukkaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']

class BakeryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(DrinkCategory, DrinksCategoryAdmin)
admin.site.register(BakeryCategory, BakeryCategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Drink, DrinksAdmin)
admin.site.register(Hukka, HukkaAdmin)
admin.site.register(Beakery, BakeryAdmin)
