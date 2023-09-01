from typing import Iterable, Optional
from django.db import models

# Create your models here.

class Futsal(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    date = models.DateField(blank=False, null=False)
    start_time = models.TimeField(blank=False, null=False)
    end_time = models.TimeField(blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    paid = models.BooleanField(default=False, blank=False, null=False)

    def __str__(self):
        return self.name
