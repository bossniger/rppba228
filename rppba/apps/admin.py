from django.contrib import admin
# Register your models here.
from django.contrib.auth import get_user_model
from django.contrib.admin import AdminSite
from .product.models import Product, Component, Material

admin.site.register(Material)
admin.site.register(Component)
admin.site.register(Product)
