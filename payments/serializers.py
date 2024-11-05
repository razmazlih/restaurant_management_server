from rest_framework import serializers
from .models import Payment
from orders.serializers import OrderSerializer

class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Payment
        fields = ['id', 'order', 'payment_method', 'status', 'created_at']

    def validate_payment_method(self, value):
        valid_payment_methods = ['credit_card', 'paypal', 'cash']
        if value not in valid_payment_methods:
            raise serializers.ValidationError(f"Invalid payment method. Choose one of: {', '.join(valid_payment_methods)}.")
        return value