from django.contrib import admin
from .models import Table, Reservation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats')
    search_fields = ('number',)
    list_filter = ('seats',)

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('table', 'date_time')
    list_filter = ('date_time', 'table')
    search_fields = ('table__number',)
    ordering = ('-date_time',)