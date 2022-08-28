from rest_framework.serializers import ModelSerializer
from .models import Event
from comptes.serializers import ClientSerializer, UserSerializer
 
class EventSerializer(ModelSerializer):
    # client_id = ClientSerializer()
    # support_contact_id = UserSerializer()
    
    class Meta:
        model = Event
        fields = ['id', 'date_created', 'date_updated', 'event_status', 'event_date', 'attendess', 'notes', 
        'client_id', 'support_contact_id']
