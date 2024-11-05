from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('order', 'amount', 'payment_method', 'status', 'created_at')
    list_filter = ('payment_method', 'status')
    search_fields = ('order__id', 'status')
    readonly_fields = ('amount', 'created_at')  # כדי למנוע עריכת amount

    def has_add_permission(self, request):
        return False  # למנוע יצירת תשלומים חדשים ישירות בממשק הניהול

admin.site.register(Payment, PaymentAdmin)