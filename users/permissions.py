from rest_framework.permissions import BasePermission, SAFE_METHODS, exceptions


class IsAdminUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        message = "Access denied, you are not an administrator"
        if request.method in SAFE_METHODS:
            return True
        elif not request.user.is_superuser:
            raise exceptions.PermissionDenied(detail=message)
        return True


class IsOwnerOrAdmin(BasePermission):
    message = "Access denied, you are not an administrator"

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        raise exceptions.PermissionDenied(detail=self.message)

    def has_object_permission(self, request, view, obj):
        if obj.user == request.user or request.user.is_superuser:
            return True
        return False
