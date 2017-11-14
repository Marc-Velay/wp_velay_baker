# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from api.serializers import ItemSerializer,BucketlistSerializer
from api.models import Item,Bucketlist
import datetime

# Create your views here.

class CreateView(generics.ListCreateAPIView):

    # Gives us control over our api
    queryset = Item.objects.filter(id__lte=100)
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new Item."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    # Handles REST ( GET, PUT, DELETE )
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class item_year(generics.ListCreateAPIView):

    #Fetch correct item serializer
    serializer_class = ItemSerializer

    def get_queryset(self):
        """
        This view returns all entries for the given year through the URL
        """
        item = self.kwargs['item']
        year = self.kwargs['year']
        return Item.objects.filter(name = item, timestamp__year = year)[:100]

class item_month(generics.ListCreateAPIView):

    #Fetch correct item serializer
    serializer_class = ItemSerializer

    def get_queryset(self):
        """
        This view returns all entries for the given month for the given item through the URL
        """
        item = self.kwargs['item']
        year = self.kwargs['year']
        month = self.kwargs['month']
        return Item.objects.filter(name = item, timestamp__year = year, timestamp__month = month)[:100]

class item_day(generics.ListCreateAPIView):

    #Fetch correct item serializer
    serializer_class = ItemSerializer

    def get_queryset(self):
        """
        This view returns all entries for the given day through the URL
        """
        item = self.kwargs['item']
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        return Item.objects.filter(name = item, timestamp__year = year, timestamp__month = month, timestamp__day = day)[:100]
