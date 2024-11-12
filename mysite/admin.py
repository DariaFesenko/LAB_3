from django.contrib import admin
from .models import Medicine, Supplier, Order, Prescription, Client, Pharmacist

class IDFilter(admin.SimpleListFilter):
    title = 'ID'
    parameter_name = 'id'
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(id=self.value())
        return queryset

class ClientAdmin(admin.ModelAdmin):
     search_fields = ('id', 'first_name', 'last_name', 'email')    
     list_filter = (IDFilter,)

admin.site.register(Client, ClientAdmin)
admin.site.register(Medicine)
admin.site.register(Supplier)
admin.site.register(Order)
admin.site.register(Prescription)
admin.site.register(Pharmacist)
