from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from payment.models import CafePayments, Order

# Register your models here.
class CafePaymentAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'total_amount', 'paid']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'order_number':
            existing_order_numbers = CafePayments.objects.values_list('order_number__id', flat=True)
            kwargs['queryset'] = Order.objects.exclude(id__in=existing_order_numbers)
        
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
admin.site.register(CafePayments, CafePaymentAdmin)