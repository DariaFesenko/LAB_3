from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum
from rest_framework.authtoken.models import Token
from .models import Supplier, Medicine, Client, Prescription, Order, Pharmacist
from .forms import SupplierForm, MedicineForm, ClientForm, PrescriptionForm, OrderForm, PharmacistForm
from .serializers import PrescriptionSerializer, SupplierSerializer, MedicineSerializer, ClientSerializer, OrderSerializer, PharmacistSerializer

def home(request):
    return HttpResponse("Hello, world!")

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer
    
class PharmacistViewSet(viewsets.ModelViewSet):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['get'])
    def aggregate_data(self, request):
        data = Order.objects.aggregate(
            total_orders=Count('id'),
            total_quantity=Sum('quantity')
        )
        return Response(data)
    
class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier_list.html'

class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'supplier_form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    template_name = 'supplier_confirm_delete.html'
    success_url = reverse_lazy('supplier_list')

class MedicineListView(ListView):
    model = Medicine
    template_name = 'medicine_list.html'
    context_object_name = 'medicines'

class MedicineDetailView(DetailView):
    model = Medicine
    template_name = 'medicine_detail.html'
    context_object_name = 'medicine'

class MedicineCreateView(CreateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine_form.html'
    success_url = reverse_lazy('medicine_list')

class MedicineUpdateView(UpdateView):
    model = Medicine
    form_class = MedicineForm
    template_name = 'medicine_form.html'
    success_url = reverse_lazy('medicine_list')

class MedicineDeleteView(DeleteView):
    model = Medicine
    template_name = 'medicine_confirm_delete.html'
    success_url = reverse_lazy('medicine_list')

class ClientListView(ListView):
    model = Client
    template_name = 'client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html'
    context_object_name = 'client'

class ClientCreateView(CreateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')

class ClientUpdateView(UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'client_form.html'
    success_url = reverse_lazy('client_list')

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = reverse_lazy('client_list')

class PrescriptionListView(ListView):
    model = Prescription
    template_name = 'prescription_list.html'
    context_object_name = 'prescriptions'

class PrescriptionDetailView(DetailView):
    model = Prescription
    template_name = 'prescription_detail.html'
    context_object_name = 'prescription'

class PrescriptionCreateView(CreateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'prescription_form.html'
    success_url = reverse_lazy('prescription_list')

class PrescriptionUpdateView(UpdateView):
    model = Prescription
    form_class = PrescriptionForm
    template_name = 'prescription_form.html'
    success_url = reverse_lazy('prescription_list')

class PrescriptionDeleteView(DeleteView):
    model = Prescription
    template_name = 'prescription_confirm_delete.html'
    success_url = reverse_lazy('prescription_list')

class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'
    context_object_name = 'orders'

class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'
    context_object_name = 'order'

class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')

class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order_form.html'
    success_url = reverse_lazy('order_list')

class OrderDeleteView(DeleteView):
    model = Order
    template_name = 'order_confirm_delete.html'
    success_url = reverse_lazy('order_list')

class PharmacistListView(ListView):
    model = Pharmacist
    template_name = 'pharmacist_list.html'
    context_object_name = 'pharmacists'

class PharmacistDetailView(DetailView):
    model = Pharmacist
    template_name = 'pharmacist_detail.html'
    context_object_name = 'pharmacist'

class PharmacistCreateView(CreateView):
    model = Pharmacist
    form_class = PharmacistForm
    template_name = 'pharmacist_form.html'
    success_url = reverse_lazy('pharmacist_list')

class PharmacistUpdateView(UpdateView):
    model = Pharmacist
    form_class = PharmacistForm
    template_name = 'pharmacist_form.html'
    success_url = reverse_lazy('pharmacist_list')

class PharmacistDeleteView(DeleteView):
    model = Pharmacist
    template_name = 'pharmacist_confirm_delete.html'
    success_url = reverse_lazy('pharmacist_list')
