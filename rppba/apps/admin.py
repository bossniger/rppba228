from django.contrib import admin

# Register your models here.
from django.contrib.admin import AdminSite
from .product.models import Product, Component, Material
# from .user.models import User


class RppbaAdminSite(AdminSite):
    site_header = 'Rppba Admin'
    site_title = 'Rppba Admin Portal'


rppba_admin = RppbaAdminSite(name='rppba_admin')
rppba_admin.register(Material)
rppba_admin.register(Component)
rppba_admin.register(Product)
# rppba_admin.register(User)

