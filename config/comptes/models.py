from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_staff = models.BooleanField(default=False)

class Sales(User):
    is_sales = models.BooleanField(default=True)
    class Meta:
        ordering=['last_name']
        db_table = 'Sales'
        verbose_name = 'Sales'

class Support(User):
    is_support = models.BooleanField(default=True)
    class Meta:
        ordering=['last_name']
        db_table = 'Support'
        verbose_name = 'Support'

class Client(models.Model): 
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, max_length=255, on_delete=models.PROTECT, verbose_name='ID Sales')
    first_name = models.CharField(max_length=25, verbose_name='Prenom')
    last_name = models.CharField(max_length=25, verbose_name='Nom')
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20, blank=True)
    mobile = models.CharField(max_length=20)
    company_name = models.CharField(max_length=250, verbose_name='Entreprise')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Date de modification')
    client_confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}' 
    
    class Meta:
        ordering = ['last_name']
        db_table = 'Client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    