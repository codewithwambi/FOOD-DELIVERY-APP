from rest_framework import serializers
from .models import User,Restaurant, MenuItem, Order, Delivery

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'groups', 'user_permissions']
        # If you want to show group and permissions as strings, you can customize further


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'address', 'description']
        

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'description', 'price', 'restaurant']


class OrderSerializer(serializers.ModelSerializer):
    # Nested serialization for items if needed, else use primary keys
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=MenuItem.objects.all())
    customer = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Order
        fields = ['id', 'customer', 'items', 'total_price', 'status', 'created_at']


class DeliverySerializer(serializers.ModelSerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    delivery_person = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required=False)

    class Meta:
        model = Delivery
        fields = ['id', 'order', 'delivery_person', 'status', 'location']
        
        
        
