from django.contrib import admin
from .models import Medicine, Supplier, Order, Prescription, Client, Pharmacist

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number', 'email', 'gender')
    search_fields = ('id', 'first_name', 'last_name', 'email')
admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Prescription)
admin.site.register(Pharmacist)