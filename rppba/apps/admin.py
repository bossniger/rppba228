from django.contrib import admin
from .models import User

# Register your models here.
from .product.models import Product, Component, Material
from .plan.models import Plan

admin.site.register(User)
admin.site.register(Material)
admin.site.register(Component)
admin.site.register(Product)
admin.site.register(Plan)
