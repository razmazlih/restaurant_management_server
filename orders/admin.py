from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'created_at', 'total_price')
    search_fields = ('customer__username',)  # מאפשר חיפוש לפי שם המשתמש
    date_hierarchy = 'created_at'  # מאפשר סינון לפי תאריך ההזמנה

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'menu_item', 'quantity', 'price')
    search_fields = ('order__id', 'menu_item__name')  # מאפשר חיפוש לפי מזהה הזמנה ושם פריט