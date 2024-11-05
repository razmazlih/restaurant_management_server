from rest_framework import serializers
from .models import FoodOrder, OrderItem
from menu.models import MenuItem

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = serializers.SlugRelatedField(queryset=MenuItem.objects.all(), slug_field='item')
    price_per_unit = serializers.ReadOnlyField(source='price_per_unit')
    total_price = serializers.ReadOnlyField()

    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price_per_unit', 'total_price']

class FoodOrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    total_price = serializers.ReadOnlyField()
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = FoodOrder
        fields = ['id', 'user', 'address', 'order_date', 'delivery_date', 'status', 'total_price', 'items']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        food_order = FoodOrder.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=food_order, **item_data)
        food_order.total_price = food_order.calculate_total_price()
        food_order.save()
        return food_order