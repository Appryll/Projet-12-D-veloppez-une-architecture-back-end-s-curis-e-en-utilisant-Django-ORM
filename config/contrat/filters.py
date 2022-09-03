import django_filters
from .models import Contrat
from django.db.models import Q

class ContratFilter(django_filters.FilterSet):
    client_filter = django_filters.CharFilter(method='filter_client')

    class Meta:
        model = Contrat
        fields = ['date_created', 'amount', 'client_filter']
        
    def filter_client(self, qs, name, value):
        return qs.filter(
            Q(client_id__last_name__icontains=value) | Q(client_id__email__icontains=value)
        )
        