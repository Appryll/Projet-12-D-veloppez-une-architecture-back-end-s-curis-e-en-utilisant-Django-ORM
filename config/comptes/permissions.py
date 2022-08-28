from rest_framework.permissions import BasePermission
from .models import Client
from rest_framework.generics import get_object_or_404

class IsAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_superuser)

class IsSalesAuthenticated(BasePermission):
    def has_permission(self, request, obj):
        #client = get_object_or_404(Client, id=view.kwargs.get('id'))
       
        return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_sales and
                    request.user == obj.sales_contact)
        
