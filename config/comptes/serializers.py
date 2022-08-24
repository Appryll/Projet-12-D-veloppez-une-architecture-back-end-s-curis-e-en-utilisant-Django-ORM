from rest_framework.serializers import ModelSerializer
from .models import Client, Support, Sales

class SupportSerializer(ModelSerializer):
    class Meta:
        model = Support
        fields = '__all__'

class SalesSerializer(ModelSerializer):
    class Meta:
        model = Sales
        fields = '__all__'

class ClientSerializer(ModelSerializer):
    sales_contact = SalesSerializer()
    
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 
        'date_updated', 'client_confirmed',  'sales_contact']