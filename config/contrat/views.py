from .serializers import ContratSerializer
from .models import Contrat
from comptes.models import Client

from rest_framework import viewsets, filters
from comptes.permissions import IsAdminAuthenticated, IsSalesAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ContratList(viewsets.ModelViewSet):
    serializer_class = ContratSerializer
    queryset = Contrat.objects.all()
    permission_classes = [IsAdminAuthenticated|IsSalesAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_fields = ('date_created', 'amount',)
    search_fields = ('client_id__last_name', 'client_id__email',)
    ordering_fields = ('date_created', 'amount',)