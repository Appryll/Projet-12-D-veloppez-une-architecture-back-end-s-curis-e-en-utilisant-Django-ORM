from .serializers import ContratSerializer
from .models import Contrat
from .filters import ContratFilter
from comptes.permissions import IsAdminAuthenticated, IsSalesAuthenticated

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend


class ContratList(viewsets.ModelViewSet):
    serializer_class = ContratSerializer
    queryset = Contrat.objects.all()
    permission_classes = [IsAdminAuthenticated|IsSalesAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = ContratFilter
    search_fields = ('client_id__last_name', 'client_id__email', 'amount', 'date_created')
    ordering_fields = ('date_created', 'amount',)
    