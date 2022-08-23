from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer, SalesSerializer, SupportSerializer
from .models import Client, Sales, Support
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated, IsAdminUser 
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend, FilterSet


class ClientFilter(FilterSet):
    class Meta:
        model = Client
        fields = ['last_name', 'email']

class ClientList(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAuthenticated]#IsSalesPermissions
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('last_name', 'email', 'company_name', 'sales_contact')
    ordering_fields = ('last_name', 'date_created')
    filterset_class = ClientFilter

class SalesList(viewsets.ModelViewSet):
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()
    permission_classes = [IsAuthenticated|IsAdminUser]
    pagination_class = PageNumberPagination

class SupportList(viewsets.ModelViewSet):
    serializer_class = SupportSerializer
    queryset = Support.objects.all()
    permission_classes = [IsAuthenticated|IsAdminUser]
    pagination_class = PageNumberPagination