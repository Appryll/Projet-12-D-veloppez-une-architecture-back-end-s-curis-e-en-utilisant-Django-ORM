from rest_framework import viewsets
from .serializers import EventSerializer
from .models import Event
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from comptes.views import ClientFilter

class EventList(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('event_date')
    search_fields = ('event_date', 'date_created')
    ordering_fields = ('event_date', 'date_created')
    filterset_class = ClientFilter
