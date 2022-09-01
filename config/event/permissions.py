from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from .models import Event
from contrat.models import Contrat

class IsSalesAuthenticated(BasePermission):
    def has_permission(self, request, obj):
       
        return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_sales)
                    
class PermissionSupport(BasePermission):
    """
    - Un accès en lecture seule à tous les événements.
    - Un droit de modification/d'accès pour tous les événements dont SUPPORT est responsable, jusqu'à ce qu'il soit terminé.
    """

    def has_permission(self, request, *args, **kwargs):
        if request.method == 'PUT':
            event = Event()
            contrat = Contrat()
            if event.event_perm_modification == False:
                if request.user and request.user.is_authenticated and request.user.is_support:
                    return True
                    # return bool(request.user and 
                    #         request.user.is_authenticated and 
                    #         request.user.is_support)
                if request.user.is_sales and event.client_id == contrat.client_id:
                    return True
            else:
                raise PermissionDenied("Vous ne pouvez pas modifier un événement terminé")   
        elif request.method == 'POST':
            raise PermissionDenied("Vous n'êtes pas autorisé à créer un événement") 
        elif request.method == 'GET':
             eventlisted = Event.objects.all()
             return eventlisted 
        else: 
            raise PermissionDenied("Vous n'êtes pas autorisé à supprimer un événement.") 
            