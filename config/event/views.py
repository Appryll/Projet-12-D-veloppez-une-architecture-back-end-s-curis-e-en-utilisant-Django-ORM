from .serializers import EventSerializer
from .models import Event

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class EventList(viewsets.ModelViewSet):
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('event_date',)
    ordering_fields = ('event_date', 'date_created')

    # def get_queryset(self):
    #     user_id = self.request.user
    #     return Event.objects.filter(support_contact_id=user_id)