from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,RestaurantViewSet, MenuItemViewSet, OrderViewSet, DeliveryViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'restaurants', RestaurantViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'deliveries', DeliveryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
