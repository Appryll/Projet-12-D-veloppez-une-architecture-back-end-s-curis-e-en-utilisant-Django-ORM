from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContratSerializer
from .models import Contrat
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from comptes.views import ClientFilter

class ContratList(viewsets.ModelViewSet):
    serializer_class = ContratSerializer
    queryset = Contrat.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('date_created', 'amount')
    search_fields = ('date_created', 'amount')
    ordering_fields = ('date_created', 'amount')
    filterset_class = ClientFilter
