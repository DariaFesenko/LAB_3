from django.contrib import admin
from .models import Client, Medicine, Supplier

admin.site.register(Client)
admin.site.register(Medicine)
admin.site.register(Supplier)
