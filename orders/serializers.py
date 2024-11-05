from rest_framework import serializers
from .models import Order, OrderItem
from menu.serializers import MenuItemSerializer

class OrderItemSerializer(serializers.ModelSerializer):
    menu_item = MenuItemSerializer()
    class Meta:
        model = OrderItem
        fields = ['id', 'menu_item', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'created_at', 'order_items', 'total_price']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order