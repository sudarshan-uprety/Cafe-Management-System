from django.contrib import admin
from order.models import Table, Order
from order.models import FoodOrder, DrinkOrder, HukkaOrder, BakeryOrder
from django.core.serializers import serialize
from django.db.models import FloatField
from django.db.models.functions import Cast
# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_name']

class FoodOrders(admin.TabularInline):
    model = FoodOrder
    extra =1
    verbose_name = "Food Orders"
    verbose_name_plural = "Food Orders"

class DrinkOrders(admin.TabularInline):
    model = DrinkOrder
    extra =1
    verbose_name = "Drink Orders"
    verbose_name_plural = "Drink Orders"

class HukkaOrders(admin.TabularInline):
    model = HukkaOrder
    extra =1
    verbose_name = "Hukka Orders"
    verbose_name_plural = "Hukka Orders"

class BakeryOrders(admin.TabularInline):
    model = BakeryOrder
    extra =1
    verbose_name = "Bakery Orders"
    verbose_name_plural = "Bakery Orders"
class OrderAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'ordered_items', 'order_by', 'order_time']

    def ordered_items(self, obj):
        food = obj.food.all().values_list('name')
        drinks = obj.drink.all().values_list('name')
        bakery = obj.bakery.all().values_list('name')
        hukka = obj.hukka.all().values_list('name')
        return list(food)+list(drinks)+list(bakery)+list(hukka)

    exclude = ['order_by', 'total_amount']
    inlines = [FoodOrders, DrinkOrders, HukkaOrders, BakeryOrders]
    def save_model(self, request, obj, form, change):
        obj.order_by = request.user
        super().save_model(request, obj, form, change)
        # food_price = obj.food.all().annotate(float_price=Cast('price', FloatField())).values_list('float_price', flat=True)
        # drinks_price = obj.drink.all().annotate(float_price=Cast('price', FloatField())).values_list('float_price', flat=True)
        # bakery_price = obj.bakery.all().annotate(float_price=Cast('price', FloatField())).values_list('float_price', flat=True)
        # hukka_price = obj.hukka.all().annotate(float_price=Cast('price', FloatField())).values_list('float_price', flat=True)
        # obj.total_amount = sum(list(food_price))+sum(list(drinks_price))+sum(list(hukka_price))+sum(list(bakery_price))
        # obj.save()

admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)