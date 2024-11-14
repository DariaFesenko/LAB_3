from django import forms
from .models import Supplier, Medicine, Client, Prescription, Order, Pharmacist

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'

class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class PharmacistForm(forms.ModelForm):
    class Meta:
        model = Pharmacist
        fields = '__all__'