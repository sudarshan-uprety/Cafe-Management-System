from django.contrib import admin
from order.models import Table, Order

# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_name']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'ordered_items', 'order_by', 'order_time']

    def ordered_items(self, obj):
        return ", ".join([item.name for item in obj.items.all()])

    exclude = ['order_by']

    def save_model(self, request, obj, form, change):
        if not change:  # Only set the order_by field if the object is being created (not changed).
            obj.order_by = request.user
        super().save_model(request, obj, form, change)

admin.site.register(Table, TableAdmin)
admin.site.register(Order, OrderAdmin)