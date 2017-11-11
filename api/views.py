# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import generics
from api.serializers import BucketlistSerializer
from api.models import Bucketlist

# Create your views here.

class CreateView(generics.ListCreateAPIView):

    # Gives us control over our api
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer

    def perform_create(self, serializer):
        """Save the post data when creating a new bucketlist."""
        serializer.save()

class DetailsView(generics.RetrieveUpdateDestroyAPIView):

    # Handles REST ( GET, PUT, DELETE )
    queryset = Bucketlist.objects.all()
    serializer_class = BucketlistSerializer
