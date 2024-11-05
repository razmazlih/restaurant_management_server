from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('staff', 'Staff'),
        ('manager', 'Manager'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_staff_member = models.BooleanField(default=False, editable=False)
    loyalty_points = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.role != 'customer':
            self.is_staff_member = True
        else:
            self.is_staff_member = False
        super().save(*args, **kwargs)

    class Meta:
        swappable = 'AUTH_USER_MODEL'