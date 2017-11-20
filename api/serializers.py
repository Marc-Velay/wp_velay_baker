from rest_framework import serializers
from api.models import Item

class ItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Item
        fields = ('id', 'name', 'source', 'timestamp','opening','high','low','closing')
