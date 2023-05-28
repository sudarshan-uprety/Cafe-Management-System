from django.contrib import admin
from category.models import FoodCategory,HukkaCategory,DrinkCategory,BeakeryCategory

# Register your models here.

class FoodCategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('category_name',)}
    list_display=['name']


class DrinkCategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('category_name',)}
    list_display=['name']

class HukkaCategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('category_name',)}
    list_display=['name']

class BeakeryCategoryAdmin(admin.ModelAdmin):
    # prepopulated_fields={'slug':('category_name',)}
    list_display=['name']




admin.site.register(FoodCategory,FoodCategoryAdmin)
admin.site.register(DrinkCategory,DrinkCategoryAdmin)
admin.site.register(HukkaCategory,HukkaCategoryAdmin)
admin.site.register(BeakeryCategory,BeakeryCategoryAdmin)
