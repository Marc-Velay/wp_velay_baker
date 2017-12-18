# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import csv
from django.db import connection
from rest_framework import generics,permissions
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from api.serializers import *
from api.models import *
import datetime

# Create your views here.

class CreateView(generics.ListCreateAPIView):

    # Gives us control over our api
    queryset = Item.objects.filter(id__lte=100)
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new Item."""
        serializer.save()

class DetailsView(generics.RetrieveAPIView):

    # Handles REST ( GET, PUT, DELETE )
    serializer_class = ItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        This view returns all entries for the given year through the URL
        """
        pk = self.kwargs['pk']
        item = Item.objects.filter(id = pk,)
        return item

class PortfolioList(generics.ListAPIView):
    """View to list the portfolio queryset."""
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class PortfolioView(generics.RetrieveUpdateDestroyAPIView):

    # Handles REST ( GET, PUT, DELETE )
    queryset = Portfolio.objects.filter(id__lte=100)
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UpdatePortfolioView(generics.UpdateAPIView):

    # Handles REST ( GET, PUT, DELETE )
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

class CreatePortfolioView(generics.CreateAPIView):

    # Gives us control over our api
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        """Save the post data when creating a new Portfolio."""
        serializer.save(user=self.request.user)

class LinkItemToPortfolio(generics.CreateAPIView):

    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        portfolio = Portfolio.objects.get(id = request.data.get('id'))
        pk = self.kwargs['pk']
        item = Item.objects.get(id=pk)
        portfolio.items.add(item)

        serializer = PortfolioSerializer(portfolio)

        return Response(serializer.data)

class RemoveItemFromPortfolio(generics.CreateAPIView):

    serializer_class = PortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        portfolio = Portfolio.objects.get(id = request.data.get('id'))
        pk = self.kwargs['pk']
        item = Item.objects.get(id=pk)
        portfolio.items.remove(item)

        serializer = PortfolioSerializer(portfolio)

        return Response(serializer.data)

class GetItemsFromPortfolio(generics.RetrieveAPIView):

    #Fetch correct item serializer
    serializer_class = PortfolioItemSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        This view returns all entries for the given year through the URL
        """
        pk = self.kwargs['pk']
        portfolio = Portfolio.objects.filter(id = pk,)
        return portfolio

class item_year(generics.ListCreateAPIView):

    #Fetch correct item serializer
    serializer_class = ForexSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        This view returns all entries for the given year through the URL
        """
        year = self.kwargs['year']
        return Forex.objects.filter(
            timestamp__year = year
        )[:100]

class item_month(generics.ListCreateAPIView):

    #Fetch correct item serializer
    serializer_class = ForexSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        This view returns all entries for the given month for the given item through the URL
        """
        year = self.kwargs['year']
        month = self.kwargs['month']
        return Forex.objects.filter(
            timestamp__year = year,
            timestamp__month = month
        )[:100]

class item_day(generics.ListCreateAPIView):

    #Fetch correct item serializer
    serializer_class = ForexSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        This view returns all entries for the given day through the URL
        """
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        return Forex.objects.filter(
            timestamp__year = year,
            timestamp__month = month,
            timestamp__day = day
        )[:100]

class item_last24(generics.ListCreateAPIView):

    #Fetch serializer
    serializer_class = ForexSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        """
        This view returns the last 24 hours of a given item
        """
        item = self.kwargs['item']
        date_from = datetime.datetime.now() - datetime.timedelta(days=1)
        return Item.objects.filter(
            name = item,
            timestamp__gte = date_from
        )[:100]

class UserAddView(generics.CreateAPIView):

    #Fetch serializer
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'username': token.user.username, 'id': token.user_id})

class UserView(generics.ListAPIView):
    """View to list the user queryset."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailsView(generics.RetrieveAPIView):
    """View to retrieve a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateView(generics.UpdateAPIView):
    """View to update a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDeleteView(generics.DestroyAPIView):
    """View to delete a user instance."""
    queryset = User.objects.all()
    serializer_class = UserSerializer
