from rest_framework.permissions import BasePermission


class IsTechnologist(BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'technologist'
