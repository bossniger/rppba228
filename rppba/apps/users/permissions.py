from rest_framework import permissions


class IsNotAuthenticated(permissions.IsAuthenticated):
    """
    Allows access only to not authenticated users.
    """

    def has_permission(self, request, view) -> bool:
        return not request.user.is_authenticated
