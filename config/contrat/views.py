from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ContratSerializer
from .models import Contrat

class ContratList(viewsets.ModelViewSet):
    serializer_class = ContratSerializer
    queryset = Contrat.objects.all()
