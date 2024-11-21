from rest_framework import viewsets, permissions
from .models import CustomUser
from .serializers import UserSerializer

from rest_framework import permissions

from rest_framework import permissions

class IsManagerOrOwnerWithPostPermission(permissions.BasePermission):
    """
    Custom permission:
    - Unauthenticated users can perform POST requests to create new users.
    - Managers (role='manager') can perform any action on all data.
    - Regular users:
        - Can modify (PUT/PATCH) only their own data.
        - Can view (GET) only their own data.
    """
    def has_permission(self, request, view):
        # Allow POST requests for unauthenticated users
        if request.method == 'POST':
            return True

        # Allow all actions for managers
        if request.user.is_authenticated and request.user.role == 'manager':
            return True

        # For other actions, ensure the user is authenticated
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Managers can access and modify all data
        if request.user.is_authenticated and request.user.role == 'manager':
            return True

        # Regular users can modify only their own data
        if request.method in ['PUT', 'PATCH']:
            return obj == request.user

        # Allow read-only access for authenticated users to their own data
        return request.user.is_authenticated and obj == request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsManagerOrOwnerWithPostPermission]

    def get_queryset(self):
        # Managers can view all users; regular users can view only their own data
        if self.request.user.is_authenticated and self.request.user.role == 'manager':
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)