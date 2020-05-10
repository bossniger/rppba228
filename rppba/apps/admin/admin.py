from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext, gettext_lazy as _
from apps.elements.models import Element
from apps.materials_order.models import MaterialOrder
from apps.orders.models import Order
from apps.products.models import Product
from apps.operations.models import (
    Operation,
    OperationsList,
    OperationsInline,
)
from apps.warehouse_materials.models import WarehouseMaterial
from users.models import User


class RppbaAdminSite(AdminSite):
    site_header = 'RPPBA Admin'
    site_title = 'RPPBA Admin Portal'
    index_title = 'Welcome to RPPBA Project '


class RppbaUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',),
        }),
        (_('Project Fields'), {
            'fields': ('role',),
        }),
    )

    list_display = ('username', 'name', 'role',)


class ProductAdmin(admin.ModelAdmin):

    list_display = ('model_name', 'type', 'product_time_production',)
    inlines = [
        OperationsInline,
    ]


class OperationsListAdmin(admin.ModelAdmin):

    list_display = ('name', 'priority', )


class OperationsAdmin(admin.ModelAdmin):

    list_display = ('operation', 'product', 'time_processing')


class ElementsAdmin(admin.ModelAdmin):

    list_display = ('name', 'type', )


rppba_admin = RppbaAdminSite(name='rpbba_admin')
admin.site.unregister(Group)
rppba_admin.register(Element, ElementsAdmin)
rppba_admin.register(User, RppbaUserAdmin)
rppba_admin.register(Product, ProductAdmin)
rppba_admin.register(Operation, OperationsAdmin)
rppba_admin.register(OperationsList, OperationsListAdmin)
rppba_admin.register(MaterialOrder)
rppba_admin.register(WarehouseMaterial)
rppba_admin.register(Order)

