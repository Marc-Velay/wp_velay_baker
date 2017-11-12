from rest_framework import serializers
from api.models import Item,Bucketlist

class BucketlistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')

class ItemSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        model = Item
        fields = ('id', 'name', 'source', 'timestamp','opening','high','low','closing')
