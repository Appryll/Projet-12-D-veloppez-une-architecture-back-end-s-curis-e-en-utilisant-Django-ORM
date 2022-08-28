from .serializers import EventSerializer
from .models import Event
from .permissions import IsSupportAuthenticated

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class EventList(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsSupportAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('event_date',)
    search_fields = ('client_id__last_name', 'client_id__email',)
    ordering_fields = ('event_date', 'date_created')
