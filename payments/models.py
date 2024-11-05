from django.db import models
from orders.models import Order

class Payment(models.Model):
    PAYMENT_METHODS = [
        ('credit_card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('cash', 'Cash'),
    ]
    
    order = models.OneToOneField(Order, on_delete=models.CASCADE, related_name="payment")
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # שדה שאינו ניתן לעריכה
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)  # שימוש ב-choices
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed')
    ], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.amount = self.order.total_price()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Payment for Order {self.order.id} - Amount: ₪{self.amount}"