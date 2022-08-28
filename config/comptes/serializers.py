from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Client, User
from django.contrib.auth.hashers import make_password

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'first_name', 'last_name', 'email', 'is_superuser', 'is_active', 'date_joined', 
        'last_login', 'role']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self, value):
        if len(value) <= 8:
            raise ValidationError('Le mot de passe doit contenir au moins 8 caractères')
        return make_password(value)

class ClientSerializer(ModelSerializer):
    #sales_contact = UserSerializer()
    class Meta:
        model = Client
        fields = ['id','first_name', 'last_name', 'email', 'phone', 'mobile', 'company_name', 'date_created', 
        'date_updated', 'client_confirmed',  'sales_contact']
        