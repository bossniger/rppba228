from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext, gettext_lazy as _
from apps.elements.models import Elements
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
    list_display = ('username', 'name', 'role', )


# class FeedbackAdmin(admin.ModelAdmin):
#     list_display = ('date_sending', 'name', 'email', 'is_influencer', 'is_processed')
#
#
# class ShoppingcardAdmin(admin.ModelAdmin):
#     list_display = ('buyer', 'collection',)
#
#
# class InvitationAdmin(admin.ModelAdmin):
#     list_display = ('influencer_link', 'date_sending',)

rppba_admin = RppbaAdminSite(name='rpbba_admin')
admin.site.unregister(Group)
rppba_admin.register(User, RppbaUserAdmin)
rppba_admin.register(Elements)
