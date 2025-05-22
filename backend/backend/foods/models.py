from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = [
        ('customer', 'Customer'),
        ('delivery', 'Delivery Staff'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='foods_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='foods_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    description = models.TextField()

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='menu_items')

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    items = models.ManyToManyField(MenuItem)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class Delivery(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    delivery_person = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('assigned', 'Assigned'),
        ('picked_up', 'Picked Up'),
        ('on_the_way', 'On the Way'),
        ('delivered', 'Delivered')
    ], default='assigned')
    location = models.CharField(max_length=255, blank=True)