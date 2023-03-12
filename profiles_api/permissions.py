from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """docstring for ClassName"""
    def has_objects_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id

class UpdateOwnStatus(permissions.BasePermission):
    """esto permite que el usuario actualise su prefil"""
    def has_objects_permissions(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user_profile_id == request.user.id
