from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer, CreateReservationSerializer

class TableViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    @action(detail=False, methods=['post'])
    def create_reservation(self, request):
        serializer = CreateReservationSerializer(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            return Response(ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED)
        
        # במידה ולא נמצא שולחן מתאים או אם יש בעיה בנתונים, נחזיר שגיאה מותאמת אישית
        if 'No available table found' in serializer.errors.get('non_field_errors', []):
            return Response(
                {"error": "לא נמצא שולחן פנוי בזמן המבוקש ובכמות המושבים הנדרשת."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)