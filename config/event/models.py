from django.db import models
from comptes.models import Support, Client

class Event(models.Model):
    PROCES = 'En procès'
    FINALISE = 'Finalisé'

    EVENT_STATUS_CHOICES = [
        (PROCES, 'En procès'),
        (FINALISE, 'Finalisé'),]

    support_contact_id = models.ForeignKey(to=Support, on_delete=models.PROTECT, verbose_name='Contact de support')
    client_id = models.ForeignKey(to=Client, on_delete=models.PROTECT, verbose_name='Nom prenom Client')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Date de creation')
    date_updated = models.DateTimeField(auto_now_add=True, verbose_name='Date de modification')
    event_status = models.CharField(max_length=20, choices=EVENT_STATUS_CHOICES, default=PROCES)
    event_date = models.DateTimeField()
    attendess = models.IntegerField()
    notes = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f'Èvénement en état : {self.event_status}, crée pour l\'entreprise : {self.client_id.company_name}. \
                    Contact de support : {self.support_contact_id.last_name}' 
        
    class Meta:
        ordering = ['date_created']
        db_table = 'Event'
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
