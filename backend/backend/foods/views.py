from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Restaurant, MenuItem, Order, Delivery
from .serializers import UserSerializer, RestaurantSerializer, MenuItemSerializer, OrderSerializer, DeliverySerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to the Food Delivery App!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]  # Or adjust as needed
    


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]  # or IsAdminUser, AllowAny, etc.


class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = DeliverySerializer
    permission_classes = [IsAuthenticated]
    

