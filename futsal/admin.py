from django.contrib import admin
from futsal.models import Futsal
import datetime
# Register your models here.

class FutsalAdmin(admin.ModelAdmin):
    list_display = ['name', 'date', 'start_time', 'end_time','paid']


    # def save_model(self, obj):
    #     if Futsal.objects.get(date = datetime.date.today(), start_time = datetime.time)
    #     return super().save_model()
admin.site.register(Futsal, FutsalAdmin)