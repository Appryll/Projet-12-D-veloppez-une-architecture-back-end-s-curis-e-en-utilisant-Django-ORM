from django.db import models
from django.conf import settings
from django.utils.html import format_html
from django.contrib.auth.models import AbstractUser

SALES = 'SALES'
SUPPORT = 'SUPPORT'

class User(AbstractUser):
    role = models.CharField(max_length=7,choices=[(SALES, SALES),(SUPPORT, SUPPORT)])
    is_sales = models.BooleanField(default=False)
    is_support = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username}: ({self.role})"

    def save(self, *args, **kwargs):
        if self.role == SALES:
            self.is_sales = True
            self.is_support = False
        elif self.role == SUPPORT:
            self.is_sales = False
            self.is_support = True
        else:
            self.is_sales = False
            self.is_support = False

        user = super(User, self)
        user.save()
        return user
        
    class Meta:
        ordering=['username']
        db_table = 'User'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Client(models.Model): 
    sales_contact = models.ForeignKey(to=settings.AUTH_USER_MODEL, max_length=255, on_delete=models.PROTECT, 
    verbose_name='Username Contact Commercial')
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

    def entreprise(self):
        if self.client_confirmed == False:
            return format_html('<span style="color:red;">{0}</span>'.format(self.company_name))
        else:
            return format_html('<span style="color:#2fc12f; ">{0}</span>'.format(self.company_name))
    
    class Meta:
        ordering = ['last_name']
        db_table = 'Client'
        verbose_name = 'Client'
        verbose_name_plural = 'Clients'
    