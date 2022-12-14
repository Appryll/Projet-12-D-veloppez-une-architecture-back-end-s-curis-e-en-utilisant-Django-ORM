from .serializers import EventSerializer
from .models import Event
from contrat.models import Contrat
from .permissions import PermissionSupport, IsSalesAuthenticated
from comptes.permissions import IsAdminAuthenticated
from .filters import EventFilter

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import ValidationError
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend


class EventList(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsSalesAuthenticated|IsAdminAuthenticated|PermissionSupport]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = EventFilter
    search_fields = ('client_id__last_name', 'client_id__email', 'event_date',)
    ordering_fields = ('event_date', 'date_created')

    def get_queryset(self):
        """
        - Admin, Sales, Support : Un accès en lecture à tous les events.
        - Support : accéder à ses events par filtrage. permissions géreé par permissions.py
        - Sales : accéder à ses events par filtrage-> CRUD
        - admin : accéder à tous les events-> CRUD
        """
        
        if self.request.user.is_authenticated == True:
            if self.action != 'list' and self.request.user.is_support == True:
                return Event.objects.filter(support_contact_id=self.request.user)
            if self.action != 'list' and self.request.user.is_sales == True:
                return Event.objects.filter(client_id__sales_contact_id=self.request.user)
            elif self.action == 'list' and self.request.user.is_support == True or self.request.user.is_sales == True \
            or self.request.user.is_superuser == True:
                return Event.objects.all()
        else: 
            raise ValidationError("detail: Authentication credentials were not provided.")
    
    def create(self, request): 
        """
        - empêche la création d'un événement si le contrat n'est pas signé
        """     
        data = request.data.copy()
        serialized_data = self.serializer_class(data=data)
        serialized_data.is_valid(raise_exception=True)     
        contrat = get_object_or_404(Contrat, pk=serialized_data.data.get('contrat_id'))
        if contrat.status_signee == True:    
            serialized_data = self.serializer_class(data=data)
            serialized_data.is_valid(raise_exception=True)
            serialized_data.save()
            return Response(serialized_data.data)
        else:
            raise ValidationError("Vous ne pouvez pas creér un événement si le contrat n\'est pas signé.")