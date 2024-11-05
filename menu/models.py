from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - ₪{self.price}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    items = models.ManyToManyField(MenuItem, related_name="categories")

    def __str__(self):
        return self.name