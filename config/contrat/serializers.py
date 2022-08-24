from rest_framework.serializers import ModelSerializer
from .models import Contrat
from comptes.serializers import ClientSerializer, SalesSerializer
 
class ContratSerializer(ModelSerializer):
    client_id = ClientSerializer()
    sales_contact_id = SalesSerializer()

    class Meta:
        model = Contrat
        fields = ['date_created', 'date_updated', 'status_signee', 'amount', 'payment_due', 'client_id', 'sales_contact_id']