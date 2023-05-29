from django.contrib import admin
from beakery.models import Beakery
# Register your models here.

class BeakeryAdmin(admin.ModelAdmin):
    list_display=['name','price','category','image','description']

admin.site.register(Beakery,BeakeryAdmin)
