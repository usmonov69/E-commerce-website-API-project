from rest_framework import permissions 

class IsAuthor(permissions.BasePermission):
	def has_object_permission(self, requset, view, obj):
		if requset.method in permissions.SAFE_METHODS:
			return True
		return obj.author == requset.user