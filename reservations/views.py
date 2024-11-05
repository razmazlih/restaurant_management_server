from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer
from datetime import datetime, timedelta

class TableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    @action(detail=False, methods=['get'])
    def check_availability(self, request):
        date_str = request.query_params.get('date')
        seats = int(request.query_params.get('seats', 1))

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        except (ValueError, TypeError):
            return Response({"error": "תאריך לא תקין"}, status=status.HTTP_400_BAD_REQUEST)

        available_tables = Table.objects.filter(seats__gte=seats)
        available_tables = [
            table for table in available_tables if table.is_available(date)
        ]

        serializer = TableSerializer(available_tables, many=True)
        return Response(serializer.data)


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        table_id = request.data.get('table')
        date_str = request.data.get('reservation_date')
        name = request.data.get('name')

        try:
            date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
        except (ValueError, TypeError):
            return Response({"error": "תאריך לא תקין"}, status=status.HTTP_400_BAD_REQUEST)

        table = Table.objects.filter(id=table_id).first()
        if not table:
            return Response({"error": "שולחן לא נמצא"}, status=status.HTTP_404_NOT_FOUND)

        if table.is_available(date):
            reservation = Reservation.objects.create(table=table, name=name, reservation_date=date)
            serializer = ReservationSerializer(reservation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "השולחן אינו פנוי בשעה זו"}, status=status.HTTP_400_BAD_REQUEST)