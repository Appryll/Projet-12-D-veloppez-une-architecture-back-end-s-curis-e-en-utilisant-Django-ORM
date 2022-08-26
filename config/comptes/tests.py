from django.urls import reverse
from .models import User
from rest_framework import status
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):

    def setUp(self):
        
        self.login_url = '/api/token/'
        self.user = User.objects.create_user(
            username='admin',
            password='superuser',
            email='contact_admin@contact.com'
        )
        
        response = self.client.post(
            self.login_url,
            {
                'username': 'admin',
                'password': 'superuser'
            },
            format='json'
        )
    
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = response.data['access']
        print(self.token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()   
    
    def test_setup(self):
        pass
