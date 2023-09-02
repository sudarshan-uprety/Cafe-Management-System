from django.contrib import admin
from order.models import Table, Order
from order.models import FoodQuantity, DrinksQuantity, HukkaQuantity, BakeryQuantity
from django.core.serializers import serialize
# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_name']

class FoodOrders(admin.TabularInline):
    model = FoodQuantity
    extra =1
    verbose_name = "Food Orders"
    verbose_name_plural = "Food Orders"

class DrinkOrders(admin.TabularInline):
    model = DrinksQuantity
    extra =1
    verbose_name = "Drink Orders"
    verbose_name_plural = "Drink Orders"

class HukkaOrders(admin.TabularInline):
    model = HukkaQuantity
    extra =1
    verbose_name = "Hukka Orders"
    verbose_name_plural = "Hukka Orders"

class BakeryOrder(admin.TabularInline):
    model = BakeryQuantity
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

    exclude = ['order_by']
    inlines = [FoodOrders, DrinkOrders, HukkaOrders, BakeryOrder]
    def save_model(self, request, obj, form, change):
        if not change:  # Only set the order_by field if the object is being created (not changed).
            obj.order_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)