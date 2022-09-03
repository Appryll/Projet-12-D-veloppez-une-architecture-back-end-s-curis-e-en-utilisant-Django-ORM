from django.db import models
from django.conf import settings

from comptes.models import Client
from contrat.models import Contrat

PROCES = 'En procès'
FINALISE = 'Finalisé'

class Event(models.Model):
    
    EVENT_STATUS_CHOICES = [
        (PROCES, 'En procès'),
        (FINALISE, 'Finalisé'),]

    support_contact_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT, 
    verbose_name='Username Contact Commercial (SUPPORT)')
    client_id = models.ForeignKey(to=Client, on_delete=models.PROTECT, verbose_name='Nom Prenom Client')
    contrat_id = models.OneToOneField(to=Contrat, on_delete=models.PROTECT, verbose_name='Contrat id')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Date de modification')
    event_status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES, default=PROCES)
    event_date = models.DateTimeField()
    attendess = models.IntegerField()
    notes = models.TextField(max_length=1000, blank=True)
    event_perm_modification = models.BooleanField(default=True)


    def __str__(self):
        return f'Èvénement en état : {self.event_status}, crée pour l\'entreprise : {self.client_id.company_name}. \
                    Contact de support : {self.support_contact_id.first_name} {self.support_contact_id.last_name}' 

    def save(self, *args, **kwargs):
        if self.event_status == PROCES:
            self.event_perm_modification = True
        else:
            self.event_perm_modification = False

        event = super(Event, self)
        event.save()
        return event 

    class Meta:
        ordering = ['-date_created']
        db_table = 'Event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
