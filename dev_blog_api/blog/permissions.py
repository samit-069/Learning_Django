from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custome Persmission to only allow author of post to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            #read only permissions allows for GET, HEAD, or OPTIOn 
            return True
        #write permission only allowed to author
        return obj.author == request.user