from django.db import models
from users.models import User
from menu.models import MenuItem
# Create your models here.


class Table(models.Model):
    table_name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.table_name


class Order(models.Model):
    table_number = models.ForeignKey(Table, on_delete=models.SET_NULL, null=True)
    order_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(MenuItem)
    order_time = models.DateTimeField(auto_now_add=True)

