from rest_framework import serializers
from .models import Table, Reservation
from datetime import datetime

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['id', 'number', 'seats']

class ReservationSerializer(serializers.ModelSerializer):
    table = TableSerializer(read_only=True)
    class Meta:
        model = Reservation
        fields = ['id', 'table', 'date_time', 'name', 'phone']

class CreateReservationSerializer(serializers.Serializer):
    seats_needed = serializers.IntegerField(required=True)
    date_time = serializers.DateTimeField()
    name = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=15)

    def validate_date_time(self, value):
        """מאמת שהשעה היא עגולה ללא דקות"""
        if value.minute != 0 or value.second != 0:
            raise serializers.ValidationError("יש לבחור שעה עגולה ללא דקות.")
        return value

    def create(self, validated_data):
        seats_needed = validated_data['seats_needed']
        date_time = validated_data['date_time']
        name = validated_data['name']
        phone = validated_data['phone']
        
        reservation = Reservation.create_reservation(seats_needed, date_time)
        
        if reservation:
            reservation.name = name
            reservation.phone = phone
            reservation.save()
            return reservation
        
        raise serializers.ValidationError("No available table found for the requested time and seating capacity.")