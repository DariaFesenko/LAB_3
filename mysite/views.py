from rest_framework import viewsets
from mysite.models import Medicine, Client, Prescription, Supplier
from .serializers import PrescriptionSerializer, MedicineSerializer, ClientSerializer
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world!")

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()

class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()  
    serializer_class = PrescriptionSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
