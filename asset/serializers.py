from rest_framework import serializers
from .models import InventoryItem, Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'