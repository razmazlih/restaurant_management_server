from django.db import models
from django.utils import timezone

class Table(models.Model):
    number = models.IntegerField(unique=True)  # מספר מזהה לשולחן
    seats = models.IntegerField()  # מספר המקומות

    def is_available(self, date_time):
        """פונקציה לבדוק אם השולחן פנוי בזמן נתון"""
        return not Reservation.objects.filter(
            table=self,
            date_time=date_time
        ).exists()

    def __str__(self):
        return f"שולחן {self.number} ({self.seats} מקומות)"

class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name="reservations")
    date_time = models.DateTimeField()
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"הזמנה לשולחן {self.table.number} בתאריך {self.date_time.strftime('%Y-%m-%d %H:%M')}"

    @staticmethod
    def create_reservation(seats_needed, date_time):
        """פונקציה לבחירת שולחן פנוי ושיבוץ הזמנה"""
        available_table = Table.objects.filter(
            seats__gte=seats_needed
        ).exclude(
            reservations__date_time=date_time
        ).first()
        
        if available_table:
            reservation = Reservation.objects.create(
                table=available_table,
                date_time=date_time
            )
            return reservation
        return None