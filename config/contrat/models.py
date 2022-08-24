from django.db import models
from comptes.models import Client, User, User
from django.conf import settings

class Contrat(models.Model):
    sales_contact_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    client_id = models.ForeignKey(to=Client, on_delete=models.PROTECT)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Date de modification')
    status_signee = models.BooleanField(default=False, verbose_name='Signee')
    amount = models.FloatField(blank=True, verbose_name='Amount')
    payment_due = models.DateTimeField(verbose_name='Date de payment')

    def __str__(self):
        if self.status_signee == True:
            return f'Contrat signée par l\'entreprise {self.client_id.company_name}.\
                     Contact commercial : {self.sales_contact_id.first_name} {self.sales_contact_id.last_name}' 
        else:
            return f'Contrat non encore signée par l\'entreprise {self.client_id.company_name}.\
                     Contact commercial : {self.sales_contact_id.first_name} {self.sales_contact_id.last_name}' 
     
    class Meta:
        ordering = ['-date_created']
        db_table = 'Contrat'
        verbose_name = 'Contrat'
        verbose_name_plural = 'Contrats'