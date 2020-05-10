from rest_framework.permissions import BasePermission


class IsTechnologist(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'technologist'


class IsDispatcher(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'dispatcher'


class IsMasterPaintWorkshop(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'master_paint_workshop'


class IsMasterAssemblyWorkshop(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'master_assembly_workshop'


class IsMasterPackingWorkshop(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'master_packing_workshop'
