from django.db import models

# Create your models here.

# Stock and item model
class Item(models.Model):
    name = models.CharField(max_length = 30)
    source = models.CharField(max_length = 30)
    timestamp = models.DateTimeField()
    opening = models.DecimalField(decimal_places=10)
    high = models.DecimalField(decimal_places=10)
    low = models.DecimalField(decimal_places=10)
    closing =  models.DecimalField(decimal_places=10)
