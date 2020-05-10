from rest_framework.permissions import BasePermission


class IsTechnologist(BasePermission):

    def has_permission(self, request, view):
        print('request.user.role')
        return request.user.role == 'technologist'
