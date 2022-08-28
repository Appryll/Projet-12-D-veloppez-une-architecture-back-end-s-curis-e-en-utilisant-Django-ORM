from .serializers import ClientSerializer, UserSerializer
from .models import Client, User
from .permissions import IsAdminAuthenticated, IsSalesAuthenticated

from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend, FilterSet


class ClientFilter(FilterSet):
    class Meta:
        model = Client
        fields = ['last_name', 'email']

class ClientList(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [IsAdminAuthenticated|IsSalesAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('last_name', 'date_created')
    filterset_class = ClientFilter

class UserList(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminAuthenticated]
    pagination_class = PageNumberPagination
    