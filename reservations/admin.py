from django.contrib import admin
from .models import Table, Reservation

class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats')
    search_fields = ('number',)
    list_filter = ('seats',)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('table', 'user', 'reservation_date', 'duration')
    list_filter = ('reservation_date', 'table')
    search_fields = ('user__username', 'table__number')

admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)