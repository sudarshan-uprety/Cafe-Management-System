from django.db import models
from order.models import Order

# Create your models here.
class CafePayments(models.Model):
    order_number = models.OneToOneField(Order, on_delete=models.PROTECT)
    total_amount = models.FloatField(blank=False, null=True)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.order_number)