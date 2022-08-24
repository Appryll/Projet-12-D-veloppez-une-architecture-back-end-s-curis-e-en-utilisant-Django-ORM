from rest_framework.permissions import BasePermission
from comptes.models import Sales
from rest_framework.generics import get_object_or_404
 
class IsAdminAuthenticated(BasePermission):
 
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_superuser)

class IsSalesPermissions(BasePermission):
    
    def has_permission(self, request, view):
        sales = get_object_or_404(Sales, id=view.kwargs['id'])
        if request.user.id == sales.user_ptr_id:
            if sales.is_sales == True:
                return True
            return False