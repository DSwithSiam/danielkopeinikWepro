from rest_framework import permissions

class IsAdminOrOwner(permissions.BasePermission):
    """
    Custom permission to only allow admins or owners of an object to edit/view it.
    """

    def has_permission(self, request, view):
        # Allow all authenticated users for list or create views,
        # object-level permission will be checked later.
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        # Admin can do anything
        if request.user.role == 'admin':
            return True
        # Otherwise, only allow if user owns the object
        return obj.user == request.user
