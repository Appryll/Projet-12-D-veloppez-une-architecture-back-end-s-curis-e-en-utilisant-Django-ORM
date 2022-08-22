from rest_framework.serializers import ModelSerializer
from .models import Client, Support, Sales
 
class ClientSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class SupportSerializer(ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'

class SalesSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'
