from rest_framework import serializers
from .models import MenuItem, Category

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'is_available']

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("The price must be greater than zero.")
        return value

class CategorySerializer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'items']