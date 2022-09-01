import django_filters
from .models import Event

class EventFilter(django_filters.FilterSet):
    
    class Meta:
        model = Event
        fields = ['event_date', 'client_id__last_name', 'client_id__email']
        