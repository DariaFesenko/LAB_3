from django.urls import path
from .views import (
    ClientListView, ClientDetailView, ClientCreateView,
    ClientUpdateView, ClientDeleteView
)

app_name = 'pharmacy'

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('clients/new/', ClientCreateView.as_view(), name='client_create'),
    path('clients/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_edit'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),
]