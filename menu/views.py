from rest_framework import viewsets
from .models import MenuCategory, MenuItem
from .serializers import MenuCategorySerializer, MenuItemSerializer
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsManagerOrReadOnly(BasePermission):
    """
    הרשאה מותאמת אישית המאפשרת עריכה רק אם תפקיד המשתמש הוא 'manager'
    """
    def has_permission(self, request, view):
        # מאפשר גישה לכל המשתמשים עבור פעולות צפייה בלבד
        if request.method in SAFE_METHODS:
            return True
        # מאפשר עריכה רק אם תפקיד המשתמש הוא "manager"
        return request.user.role == 'manager'

class MenuCategoryViewSet(viewsets.ModelViewSet):
    queryset = MenuCategory.objects.all()
    serializer_class = MenuCategorySerializer
    permission_classes = [IsManagerOrReadOnly]

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsManagerOrReadOnly]