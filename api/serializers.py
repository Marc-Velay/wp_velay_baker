from rest_framework import serializers
from api.models import Item
from django.contrib.auth.models import User


class ItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Item
        fields = ('id', 'name', 'source', 'timestamp','opening','high','low','closing')

class UserSerializer(serializers.ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    iteù = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Item.objects.all())

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('id', 'username', 'item')
