from rest_framework.serializers import ModelSerializer
from .models import Client, User

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ClientSerializer(ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 
        'date_updated', 'client_confirmed',  'user']