from rest_framework.permissions import BasePermission
from .models import Client

class IsAdminAuthenticated(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_superuser)

class PermissionSales(BasePermission):
    """
    - Un accès en lecture seule à tous les clients/contrats.
    - Un droit de modification/d'accès/de supprimer tous les clients/contrats dont SALES est responsable.
    """

    def has_permission(self, request, *args, **kwargs):
        if request.method in ['PUT', 'POST', 'DELETE']:
            return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_sales)           
        else: 
            listed = Client.objects.all()
            return listed
                    