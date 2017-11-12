# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Bucketlist(models.Model):
    """This class represents the bucketlist model."""
    name = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

# Stock and item model
class Item(models.Model):
    name = models.CharField(max_length = 30)
    source = models.CharField(max_length = 30)
    timestamp = models.DateTimeField()
    opening = models.DecimalField(max_digits=20,decimal_places=10)
    high = models.DecimalField(max_digits=20,decimal_places=10)
    low = models.DecimalField(max_digits=20,decimal_places=10)
    closing =  models.DecimalField(max_digits=20,decimal_places=10)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)
