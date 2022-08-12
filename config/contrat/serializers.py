from rest_framework.serializers import ModelSerializer
from .models import Contrat
 
class ContratSerializer(ModelSerializer):
    class Meta:
        model = Contrat
        fields = '__all__'
