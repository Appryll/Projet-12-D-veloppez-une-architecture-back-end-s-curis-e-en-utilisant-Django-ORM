from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ClientSerializer, SalesSerializer, SupportSerializer
from .models import Client, Sales, Support


class ClientList(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

class SalesList(viewsets.ModelViewSet):
    serializer_class = SalesSerializer
    queryset = Sales.objects.all()

class SupportList(viewsets.ModelViewSet):
    serializer_class = SupportSerializer
    queryset = Support.objects.all()