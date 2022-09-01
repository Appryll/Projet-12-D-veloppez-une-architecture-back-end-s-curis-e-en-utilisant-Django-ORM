from .serializers import ContratSerializer
from .models import Contrat
from .filters import ContratFilter
from comptes.permissions import IsAdminAuthenticated, PermissionSales

from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.serializers import ValidationError

from django_filters.rest_framework import DjangoFilterBackend


class ContratList(viewsets.ModelViewSet):
    serializer_class = ContratSerializer
    queryset = Contrat.objects.all()
    permission_classes = [IsAdminAuthenticated|PermissionSales]
    pagination_class = PageNumberPagination
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = ContratFilter
    search_fields = ('client_id__last_name', 'client_id__email', 'amount', 'date_created')
    ordering_fields = ('date_created', 'amount',)

    
    def get_queryset(self):
        """
        - Admin, Sales, Support : Un accès en lecture à tous les events.
        - Sales : accéder à ses contrats par filtrage-> CRUD
        - admin : accéder à tous les contrats-> CRUD
        """
        if self.request.user.is_authenticated == True:
            if self.action != 'list' and self.request.user.is_sales == True:
                return Contrat.objects.filter(sales_contact_id=self.request.user)
            if self.action != 'list' and self.request.user.is_support == True:
                raise ValidationError('Vous n\'êtes pas autorisé à accéder aux informations détaillées')
            elif self.action == 'list' and self.request.user.is_support == True or self.request.user.is_sales == True \
            or self.request.user.is_superuser == True:
                return Contrat.objects.all()
        else: 
            raise ValidationError("detail: Authentication credentials were not provided.")
            