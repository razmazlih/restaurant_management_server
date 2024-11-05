from django.contrib import admin
from .models import FoodOrder, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1

class FoodOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'address', 'order_date', 'delivery_date', 'status', 'total_price']
    list_filter = ['status', 'order_date']
    search_fields = ['user__username', 'address']
    inlines = [OrderItemInline]

admin.site.register(FoodOrder, FoodOrderAdmin)