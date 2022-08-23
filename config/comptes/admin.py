from django.contrib import admin
from .models import Client, User, Support, Sales

class ClientAdmin(admin.ModelAdmin):
    list_display=("first_name", "nom", "email", "mobile", "company_name", "date_created", "date_updated",
    "sales_contact", "client_confirmed")
    search_fields=("first_name", "last_name", "email", "company_name")

    def nom(self, obj):
        return obj.last_name.upper()
    

# Register your models here.
admin.site.register(Client, ClientAdmin)
admin.site.register(User)
admin.site.register(Support)
admin.site.register(Sales)