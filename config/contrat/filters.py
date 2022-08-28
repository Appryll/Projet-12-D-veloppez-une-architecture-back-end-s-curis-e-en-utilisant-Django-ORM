import django_filters
from .models import Contrat

class ContratFilter(django_filters.FilterSet):
    class Meta:
        model = Contrat
        fields = ['date_created', 'amount', 'client_id__last_name', 'client_id__email']
        