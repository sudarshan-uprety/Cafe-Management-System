from django.contrib import admin
from hukka.models import Hukka
# Register your models here.

class HukkaAdmin(admin.ModelAdmin):
    list_display=['name','price','category','image','description']


admin.site.register(Hukka,HukkaAdmin)