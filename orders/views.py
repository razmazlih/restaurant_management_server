from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import FoodOrder
from .serializers import FoodOrderSerializer

class FoodOrderViewSet(viewsets.ModelViewSet):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff_member:
            return self.queryset.all()
        return self.queryset.filter(user=user)