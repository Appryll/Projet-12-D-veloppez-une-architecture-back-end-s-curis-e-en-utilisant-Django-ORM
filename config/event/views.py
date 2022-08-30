from .serializers import EventSerializer
from .models import Event
from .permissions import PermissionSupport, IsSalesAuthenticated
from comptes.permissions import IsAdminAuthenticated
from .filters import EventFilter

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

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
        if self.action != 'list' and self.request.user.is_support == True:
            return Event.objects.filter(support_contact_id=self.request.user)
        elif self.action == 'list' and self.request.user.is_support == True or self.request.user.is_sales == True:
            return Event.objects.all()
