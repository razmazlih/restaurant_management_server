from rest_framework import serializers
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'role', 'email', 'address', 'city', 'phone_number', 'loyalty_points', 'is_staff_member']