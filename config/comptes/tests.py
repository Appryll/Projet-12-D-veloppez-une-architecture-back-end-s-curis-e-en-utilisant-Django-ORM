from django.urls import reverse
from .models import User
from rest_framework import status
from rest_framework.test import APITestCase

class TestSetUp(APITestCase):

    def test_get_token(self):
        
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
        # print(self.token)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        return super().setUp()   

class TestAddNewUser(TestSetUp):
    def test_new_user(self):
        self.login_url = '/user/'

        data = {'username':'admin',
            'password':'superuser',
            'email':'contact_admin@contact.com',
            'role':'SALES',}

        response = self.client.post(
            self.login_url,
            data,
            format='json',
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)