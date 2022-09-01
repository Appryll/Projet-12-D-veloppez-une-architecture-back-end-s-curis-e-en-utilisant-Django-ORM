from rest_framework.serializers import ModelSerializer
from .models import Contrat
from comptes.serializers import ClientSerializer, UserSerializer
 
class ContratSerializer(ModelSerializer):
    # client_id = ClientSerializer()
    # sales_contact_id = UserSerializer()

    class Meta:
        model = Contrat
        fields = ['id', 'date_created', 'date_updated', 'status_signee', 'amount', 'payment_due', 'client_id', 'sales_contact_id']
    