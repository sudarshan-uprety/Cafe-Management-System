from django.contrib import admin
from menu.models import Drink, Hukka, Beakery, Food, FoodCategory, HukkaCategory, BeakeryCategory, DrinkCategory

# Register your models here.

class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class DrinksCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class HukkaCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class BeakeryCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class DrinksAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class HukkaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']

class BeakeryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



admin.site.register(FoodCategory, FoodCategoryAdmin)
admin.site.register(DrinkCategory, DrinksCategoryAdmin)
admin.site.register(HukkaCategory, HukkaCategoryAdmin)
admin.site.register(BeakeryCategory, BeakeryCategoryAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Drink, DrinksAdmin)
admin.site.register(Hukka, HukkaAdmin)
admin.site.register(Beakery, BeakeryAdmin)
