from django.contrib import admin
from .models import Contrat

class ContratAdmin(admin.ModelAdmin):
    list_display=("id", '__str__')


    def __str__(self):
        if self.status_signee == True:
            return f'Contrat signée par l\'entreprise {self.client_id.company_name}.\
                     Contact commercial : {self.sales_contact_id.first_name} {self.sales_contact_id.last_name}' 
        else:
            return f'Contrat non encore signée par l\'entreprise {self.client_id.company_name}.\
                     Contact commercial : {self.sales_contact_id.first_name} {self.sales_contact_id.last_name}' 

admin.site.register(Contrat, ContratAdmin)
