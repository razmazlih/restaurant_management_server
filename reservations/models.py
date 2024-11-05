from django.db import models
from django.utils import timezone
from datetime import timedelta
from users.models import CustomUser

class Table(models.Model):
    number = models.IntegerField(unique=True)  # מספר מזהה של השולחן
    seats = models.IntegerField()  # מספר מקומות בשולחן

    def is_available(self, date, duration=timedelta(hours=2)):
        start_time = date
        end_time = date + duration

        # בדיקת זמינות לפי הזמנות קיימות
        overlapping_reservations = Reservation.objects.filter(
            table=self,
            reservation_date__lt=end_time,
            reservation_date__gte=start_time - models.F('duration')
        )

        return not overlapping_reservations.exists()

    def __str__(self):
        return f"שולחן {self.number} - {self.seats} מקומות"


class Reservation(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # מקשר משתמש להזמנה
    reservation_date = models.DateTimeField(default=timezone.now)  # או כל ערך אחר
    duration = models.DurationField(default=timezone.timedelta(hours=2))  # משך זמן שמירת השולחן

    def __str__(self):
        return f"הזמנה לשולחן {self.table.number} בתאריך {self.reservation_date.strftime('%Y-%m-%d %H:%M')}"