from django.urls import reverse_lazy
from django.http import Http404, HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count, Sum
from .models import Supplier, Medicine, Client, Prescription, Order, Pharmacist
from .forms import SupplierForm, MedicineForm, PrescriptionForm, OrderForm, PharmacistForm, ClientForm
from .serializers import (
    PrescriptionSerializer, SupplierSerializer, MedicineSerializer, ClientSerializer,
    ClientListSerializer, ClientDetailSerializer, OrderSerializer, PharmacistSerializer
)
import requests
from django.shortcuts import render, redirect
from django.http import JsonResponse

from .NetworkHelper import NetworkHelper


def home(request):
    return HttpResponse("Hello, world!")


class MedicineViewSet(ModelViewSet):
    queryset = Medicine.objects.all()
    serializer_class = MedicineSerializer


class PharmacistViewSet(ModelViewSet):
    queryset = Pharmacist.objects.all()
    serializer_class = PharmacistSerializer


class SupplierViewSet(ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class PrescriptionViewSet(ModelViewSet):
    queryset = Prescription.objects.all()
    serializer_class = PrescriptionSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(detail=False, methods=['get'])
    def aggregate_data(self, request):
        data = Order.objects.aggregate(
            total_orders=Count('id'),
            total_quantity=Sum('quantity')
        )
        return Response(data)
    
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
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


class SupplierListView(ListView):
    model = Supplier
    template_name = 'supplier_list.html'
    context_object_name = 'suppliers'


class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'supplier_detail.html'
    context_object_name = 'supplier'


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


def api_agent_view(request):
    api1 = NetworkHelper("http://127.0.0.1:8001/api/agents/", "http://127.0.0.1:8001/api/clients/", api_key="API_KEY_1")

    try:
        list_data_1 = api1.get_list(api_id=1)
        item_data_1 = api1.get_item_by_id(api_id=1, item_id=1)
        new_item_1 = api1.create_item(api_id=1, data={"name": "New Agent", "email": "agent@example.com", "phone": "123456789"})
        updated_item_1 = api1.update_item_by_id(api_id=1, item_id=1, data={"name": "Updated Agent", "email": "updated@example.com", "phone": "987654321"})
        delete_response_1 = api1.delete_item_by_id(api_id=1, item_id=1)

        list_data_2 = api1.get_list(api_id=2)
        item_data_2 = api1.get_item_by_id(api_id=2, item_id=1)
        new_item_2 = api1.create_item(api_id=2, data={"name": "New Client", "email": "client@example.com", "phone": "123456789"})
        updated_item_2 = api1.update_item_by_id(api_id=2, item_id=1, data={"name": "Updated Client", "email": "updated@example.com", "phone": "987654321"})
        delete_response_2 = api1.delete_item_by_id(api_id=2, item_id=1)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({
        "api_1": {
            "list_data": list_data_1,
            "item_data": item_data_1,
            "new_item": new_item_1,
            "updated_item": updated_item_1,
            "delete_response": delete_response_1,
        },
        "api_2": {
            "list_data": list_data_2,
            "item_data": item_data_2,
            "new_item": new_item_2,
            "updated_item": updated_item_2,
            "delete_response": delete_response_2,
        },
    })
    
    import requests

API_URL = "http://127.0.0.1:8001/api/agents/"
HEADERS = {"Authorization": "Basic YWNlcjowMDQzNDQ2Njg="}

def agent_list(request):
    response = requests.get(API_URL, headers=HEADERS)
    if response.status_code == 200:
        agents = response.json()
    else:
        agents = [] 

    if request.method == "POST":
        agent_id = request.POST.get("agent_id")
        if agent_id:
            delete_url = f"{API_URL}{agent_id}/"
            delete_response = requests.delete(delete_url, headers=HEADERS)
            if delete_response.status_code == 204:
                return redirect("agent_list") 

    return render(request, "agent_list.html", {"agents": agents})

CLIENTS_API_URL = "http://127.0.0.1:8001/api/clients/" 
HEADERS = {"Authorization": "Basic YWNlcjowMDQzNDQ2Njg="} 

def client_list(request):
    response = requests.get(CLIENTS_API_URL, headers=HEADERS)
    if response.status_code == 200:
        clients = response.json()
    else:
        clients = []

    if request.method == "POST":
        client_id = request.POST.get("client_id")
        if client_id:
            delete_url = f"{CLIENTS_API_URL}{client_id}/"
            delete_response = requests.delete(delete_url, headers=HEADERS)
            if delete_response.status_code == 204:
                return redirect("client_list") 

    return render(request, "client_list.html", {"clients": clients})