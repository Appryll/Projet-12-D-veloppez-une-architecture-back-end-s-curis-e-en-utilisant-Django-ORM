from .serializers import ClientSerializer, UserSerializer
from .models import Client, User
from .permissions import IsAdminAuthenticated, PermissionSales

from rest_framework import viewsets, filters, status
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import DjangoFilterBackend, FilterSet


class ClientFilter(FilterSet):
    class Meta:
        model = Client
        fields = ['last_name', 'email']

class ClientList(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    permission_classes = [PermissionSales|IsAdminAuthenticated]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    ordering_fields = ('last_name', 'date_created')
    filterset_class = ClientFilter

    def get_queryset(self):
        """
        - Admin, Sales, Support : Un accès en lecture seule à tous les clients.
        - Sales : accéder à ses clients par filtrage.
        """
        if self.action != 'list' and self.request.user.is_sales == True:
            return Client.objects.filter(sales_contact=self.request.user)
        elif self.action == 'list' and self.request.user.is_support == True or self.request.user.is_sales == True \
        or self.request.user.is_superuser == True:
            return Client.objects.all()
        

class UserList(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminAuthenticated]
    pagination_class = PageNumberPagination
    