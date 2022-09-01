from django.contrib import admin
from .models import Event

class EventAdmin(admin.ModelAdmin):
    list_display=("id", '__str__')

    
    def __str__(self):
        return f'Èvénement en état : {self.event_status}, crée pour l\'entreprise : {self.client_id.company_name}. \
                    Contact de support : {self.support_contact_id.first_name} {self.support_contact_id.last_name}'

admin.site.register(Event, EventAdmin)
