from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from .models import Event

class IsSalesAuthenticated(BasePermission):
    def has_permission(self, request, obj):
       
        return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_sales)
                    
class PermissionSupport(BasePermission):
    """
    - Un accès en lecture seule à tous les événements.
    - Un droit de modification/d'accès pour tous les événements dont SUPPORT est responsable.
    """

    def has_permission(self, request, *args, **kwargs):
        if request.method == 'PUT':
            return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_support)       
        elif request.method == 'POST':
            raise PermissionDenied("Vous n'êtes pas autorisé à créer un événement") 
        elif request.method == 'GET':
             eventlisted = Event.objects.all()
             return eventlisted 
        else: 
            raise PermissionDenied("Vous n'êtes pas autorisé à supprimer un événement.") 
            