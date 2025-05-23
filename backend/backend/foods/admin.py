from django.contrib import admin
from .models import User, Restaurant, MenuItem, Order, Delivery

# Register models only once
models_to_register = [User, Restaurant, MenuItem, Order, Delivery]

for model in models_to_register:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass  # Skip if already registered
