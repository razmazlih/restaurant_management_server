from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuItemViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'menu_items', MenuItemViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]