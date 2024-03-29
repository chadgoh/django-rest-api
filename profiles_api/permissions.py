from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """allow users to edit only their own profile"""

    def has_object_permission(self, request, view, obj):
        """check user is editing own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """check user is editting his own post"""
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == request.user.id