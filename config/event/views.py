from .serializers import EventSerializer
from .models import Event
from .permissions import IsSupportAuthenticated
from comptes.permissions import IsAdminAuthenticated, IsSalesAuthenticated

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q


class EventList(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    permission_classes = [IsSalesAuthenticated|IsAdminAuthenticated|IsSupportAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('event_date',)
    search_fields = ('client_id__last_name', 'client_id__email',)
    ordering_fields = ('event_date', 'date_created')

    def get_queryset(self):
        if self.action != 'destroy' and self.request.user.is_support == True:
            return Event.objects.filter(support_contact_id=self.request.user)
        elif self.request.user.is_sales == True:
            return Event.objects.all()
        
 


# class EventListRestringed(viewsets.ModelViewSet):
#     serializer_class = EventListSerializer
#     permission_classes = [IsSupportAuthenticated]
#     pagination_class = PageNumberPagination
#     filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
#     filterset_fields = ('event_date',)
#     search_fields = ('client_id__last_name', 'client_id__email',)
#     ordering_fields = ('event_date', 'date_created')

#     def get_queryset(self):
#         user = self.request.user

#         queryset = queryset.filter(Q(event__support_contact_id__id=user))
#         return queryset