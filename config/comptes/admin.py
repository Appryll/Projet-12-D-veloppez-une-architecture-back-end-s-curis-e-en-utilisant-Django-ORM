from multiprocessing.connection import Client
from django.contrib import admin
from .models import User, Client

class ClientAdmin(admin.ModelAdmin):
    list_display=("first_name", "nom", "email", "mobile", "entreprise", "date_created", "date_updated",
    "sales_contact", "client_confirmed")
    ordering=('-last_name',)
    search_fields=("first_name", "last_name", "email", "entreprise")

    def nom(self, obj):
        return obj.last_name.upper()

class UserAdmin(admin.ModelAdmin):
    list_display=("username", "nom", "first_name", "email", "is_sales", "is_support", "is_superuser")
    ordering=('username','is_sales', 'is_support',)
    search_fields=("username", "first_name", "last_name", "email", "is_sales", "is_support")
    list_filter=('is_sales', 'is_support',)
    exclude=('password',)

    def nom(self, obj):
        return obj.last_name.upper()
    
admin.site.register(User, UserAdmin)
admin.site.register(Client, ClientAdmin)