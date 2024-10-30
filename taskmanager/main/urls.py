from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('clients/', views.client_list, name='client_list'),
    path('clients/add/', views.client_create, name='client_create'), 
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'),  
    path('clients/edit/<int:client_id>/', views.client_update, name='client_update'),
    path('clients/delete/<int:client_id>/', views.client_delete, name='client_delete'),  

    path('suppliers/add/', views.supplier_create, name='supplier_create'), 
    path('suppliers/edit/<int:supplier_id>/', views.supplier_update, name='supplier_update'), 
    path('suppliers/<int:supplier_id>/', views.supplier_detail, name='supplier_detail'), 
    path('suppliers/delete/<int:supplier_id>/', views.supplier_delete, name='supplier_delete'),  
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/', views.supplier_list, name='supplier_list'),

    path('medicines/', views.medicine_list, name='medicine_list'),
    path('medicines/add/', views.medicine_create, name='medicine_create'),  
    path('medicines/edit/<int:medicine_id>/', views.medicine_update, name='medicine_update'), 
    path('medicines/<int:medicine_id>/', views.medicine_detail, name='medicine_detail'),  
    
    path('orders/', views.order_list, name='order_list'),  
    path('orders/add/', views.order_create, name='order_create'),  
    path('orders/edit/<int:order_id>/', views.order_update, name='order_update'),  
    path('orders/<int:order_id>/', views.order_detail, name='order_detail'),  
    path('orders/delete/<int:order_id>/', views.order_delete, name='order_delete'),
    path('orders/', views.order_list, name='order_list'),

    path('pharmacists/', views.pharmacist_list, name='pharmacist_list'),
    path('pharmacists/add/', views.pharmacist_create, name='pharmacist_create'),
    path('pharmacists/edit/<int:pharmacist_id>/', views.pharmacist_update, name='pharmacist_update'),
    path('pharmacists/<int:pharmacist_id>/', views.pharmacist_detail, name='pharmacist_detail'),
    path('pharmacists/delete/<int:pharmacist_id>/', views.pharmacist_delete, name='pharmacist_delete'),

    path('prescriptions/', views.prescription_list, name='prescription_list'),
    path('prescriptions/add/', views.prescription_create, name='prescription_create'),
    path('prescriptions/edit/<int:prescription_id>/', views.prescription_update, name='prescription_update'),
    path('prescriptions/<int:prescription_id>/', views.prescription_detail, name='prescription_detail'),
    path('prescriptions/delete/<int:prescription_id>/', views.prescription_delete, name='prescription_delete'),

]
