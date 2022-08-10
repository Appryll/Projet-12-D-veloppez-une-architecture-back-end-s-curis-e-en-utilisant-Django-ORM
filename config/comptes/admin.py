from django.contrib import admin
from .models import Client, User, Support, Sales

# Register your models here.
admin.site.register(Client)
admin.site.register(User)
admin.site.register(Support)
admin.site.register(Sales)