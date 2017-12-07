from rest_framework import serializers
from api.models import *
from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Item
        fields = ('id', 'name', 'source', 'timestamp','opening','high','low','closing')

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('first_name','last_name','username', 'password')

class PortfolioSerializer(serializers.ModelSerializer):
    """Portfolio serializer"""
    #user = serializers.StringRelatedField(many=True)

    class Meta:
        """Map this serializer to the default portfolio model."""
        model = Portfolio
        fields = ('id','name',)
