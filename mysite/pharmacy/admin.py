
# Register your models here.
# pharmasy/admin.py

from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'gender')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
# pharmasy/admin.py


