# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from api.serializers import ItemSerializer,BucketlistSerializer
from api.models import Item,Bucketlist

# Create your views here.

class CreateView(generics.ListCreateAPIView):

    # Gives us control over our api
    queryset = Item.objects.filter(id__lte=100)
    serializer_class = ItemSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    # Handles REST ( GET, PUT, DELETE )
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
