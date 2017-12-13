from rest_framework.serializers import *
from api.models import *
from django.contrib.auth.models import User


class ItemSerializer(ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Item
        fields = ('id', 'name', 'source', 'inst_type')

class UserSerializer(ModelSerializer):
    """A user serializer to aid in authentication and authorization."""

    class Meta:
        """Map this serializer to the default django user model."""
        model = User
        fields = ('first_name','last_name','username', 'password')

class PortfolioSerializer(ModelSerializer):
    """Portfolio serializer"""
    user = SerializerMethodField()
    items = ItemSerializer(many=True, read_only=True)

    class Meta:
        """Map this serializer to the default portfolio model."""
        model = Portfolio
        fields = ('id','name','user','items')

    def get_user(self, obj):
        return str(obj.user.username)
