# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.dispatch import receiver

#Portfolio model
class Portfolio(models.Model):
    """
    Portfolio model
    """
    name = models.CharField(max_length=150, unique=True)
    #owner = models.ForeignKey(User, on_delete=models.CASCADE)

    #def __unicode__(self):
    #    return '%s' % (self.owner.username)

# Stock and item model
class Item(models.Model):
    """
    All items
    """
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

class PortfolioItem(models.Model):
    """
    An item within a portfolio.
    """

    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    Item = models.ForeignKey(Item, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('portfolio', 'Item')


# Token receiver
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
