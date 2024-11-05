from django.db import models
from django.utils import timezone
from menu.models import MenuItem
from django.db.models.signals import post_save
from django.dispatch import receiver
from users.models import CustomUser


class FoodOrder(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('DELIVERED', 'Delivered'),
        ('CANCELLED', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='food_orders')
    address = models.CharField(max_length=255)
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, editable=False)

    class Meta:
        ordering = ['-order_date']
    
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

    def calculate_total_price(self):
        return sum(item.total_price for item in self.items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(FoodOrder, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def price_per_unit(self):
        return self.menu_item.price

    @property
    def total_price(self):
        return self.quantity * self.price_per_unit

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name} for order {self.order.id}"

# Signal to update total_price after the FoodOrder is saved
@receiver(post_save, sender=FoodOrder)
def update_total_price(sender, instance, created, **kwargs):
    if created:
        instance.total_price = sum(item.total_price for item in instance.items.all())
        instance.save()