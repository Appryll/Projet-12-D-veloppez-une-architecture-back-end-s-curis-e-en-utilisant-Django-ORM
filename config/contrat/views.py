from .serializers import ContratSerializer
from .models import Contrat
from comptes.models import Client

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class ContratList(viewsets.ModelViewSet):
    serializer_class = ContratSerializer
    queryset = Contrat.objects.all()
    # permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filterset_fields = ('date_created', 'amount',)
    ordering_fields = ('date_created', 'amount',)

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Client.objects.all()
    #     first_name = self.request.query_params.get('first_name')
    #     if first_name is not None:
    #         queryset = queryset.filter(client__first_name=first_name)
    #     return queryset