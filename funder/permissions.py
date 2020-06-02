from rest_framework import permissions


class IsAccountOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read-only is allowed for any request made
        if request.method in permissions.SAFE_METHODS:
            return True

        # permission to update account info is for the owner
        return obj.username == request.user
