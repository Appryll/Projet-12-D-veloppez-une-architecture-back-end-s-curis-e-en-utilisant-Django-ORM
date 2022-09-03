import django_filters
from .models import Event
from django.db.models import Q

class EventFilter(django_filters.FilterSet):
    client_filter = django_filters.CharFilter(method='filter_client')
    
    class Meta:
        model = Event
        fields = ['event_date', 'client_filter']
    
    def filter_client(self, qs, name, value):
        return qs.filter(
            Q(client_id__last_name__icontains=value) | Q(client_id__email__icontains=value)
        )
        