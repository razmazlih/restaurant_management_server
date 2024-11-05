from django.db import models
from users.models import CustomUser
from menu.models import MenuItem  # הנחה שהמודל MenuItem נמצא באפליקציה menu
from django.db.models import Sum

class Order(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_price(self):
        total = sum(item.price for item in self.order_items.all())
        return total

    def __str__(self):
        return f"Order {self.id} by {self.customer.username} on {self.created_at.strftime('%Y-%m-%d')}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def price(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return f"{self.menu_item.name} (x{self.quantity}) for Order {self.order.id}"