from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Client

class ClientListView(ListView):
    model = Client
    template_name = 'pharmacy/client_list.html'
    context_object_name = 'clients'

class ClientDetailView(DetailView):
    model = Client
    template_name = 'pharmacy/client_detail.html'
    context_object_name = 'client'

class ClientCreateView(CreateView):
    model = Client
    template_name = 'pharmacy/client_create.html'
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'gender']
    success_url = reverse_lazy('pharmacy:client_list')
    
class ClientUpdateView(UpdateView):
    model = Client
    template_name = 'pharmacy/client_form.html'
    fields = ['first_name', 'last_name', 'phone_number', 'email', 'gender']

class ClientDeleteView(DeleteView):
    model = Client
    template_name = 'pharmacy/client_confirm_delete.html'  
    success_url = reverse_lazy('pharmacy:client_list')  