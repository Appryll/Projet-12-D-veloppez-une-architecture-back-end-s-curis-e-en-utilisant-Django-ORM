from rest_framework.permissions import BasePermission
from .models import Event
from rest_framework.generics import get_object_or_404

class IsSupportAuthenticated(BasePermission):
    def has_permission(self, request, obj):
        #client = get_object_or_404(Client, id=view.kwargs.get('id'))
        nom_username = request.user.id
        exist = Event.objects.filter(support_contact_id=nom_username).exists()
        return bool(request.user and 
                    request.user.is_authenticated and 
                    request.user.is_support and exist
                    #and request.user == obj.sales_contact_id
                    )
        
