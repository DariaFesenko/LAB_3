from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mysite.views import (
    OrderViewSet, MedicineViewSet, ClientViewSet, PrescriptionViewSet, SupplierViewSet,
    SupplierListView, SupplierDetailView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView,
    MedicineListView, MedicineDetailView, MedicineCreateView, MedicineUpdateView, MedicineDeleteView,
    ClientListView, ClientDetailView, ClientCreateView, ClientUpdateView, ClientDeleteView,
    PrescriptionListView, PrescriptionDetailView, PrescriptionCreateView, PrescriptionUpdateView, PrescriptionDeleteView,
    OrderListView, OrderDetailView, OrderCreateView, OrderUpdateView, OrderDeleteView,
    PharmacistListView, PharmacistViewSet, PharmacistDetailView, PharmacistCreateView, PharmacistUpdateView, PharmacistDeleteView,
    home   
)

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'prescriptions', PrescriptionViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'order', OrderViewSet, basename='order')
router.register(r'pharmacist', PharmacistViewSet)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('orders/aggregate_data/', OrderViewSet.as_view({'get': 'aggregate_data'}), name='order-aggregate-data'),
    # Supplier URLs
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('supplier/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/new/', SupplierCreateView.as_view(), name='supplier_create'),
    path('supplier/<int:pk>/edit/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/delete/', SupplierDeleteView.as_view(), name='supplier_delete'),

    # Medicine URLs
    path('medicines/', MedicineListView.as_view(), name='medicine_list'),
    path('medicine/<int:pk>/', MedicineDetailView.as_view(), name='medicine_detail'),
    path('medicine/new/', MedicineCreateView.as_view(), name='medicine_create'),
    path('medicine/<int:pk>/edit/', MedicineUpdateView.as_view(), name='medicine_update'),
    path('medicine/<int:pk>/delete/', MedicineDeleteView.as_view(), name='medicine_delete'),

    # Client URLs
    path('clients/', ClientListView.as_view(), name='client_list'),
    path('client/<int:pk>/', ClientDetailView.as_view(), name='client_detail'),
    path('client/new/', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>/edit/', ClientUpdateView.as_view(), name='client_update'),
    path('client/<int:pk>/delete/', ClientDeleteView.as_view(), name='client_delete'),

    # Prescription URLs
    path('prescriptions/', PrescriptionListView.as_view(), name='prescription_list'),
    path('prescription/<int:pk>/', PrescriptionDetailView.as_view(), name='prescription_detail'),
    path('prescription/new/', PrescriptionCreateView.as_view(), name='prescription_create'),
    path('prescription/<int:pk>/edit/', PrescriptionUpdateView.as_view(), name='prescription_update'),
    path('prescription/<int:pk>/delete/', PrescriptionDeleteView.as_view(), name='prescription_delete'),

    # Order URLs
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order_detail'),
    path('order/new/', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/edit/', OrderUpdateView.as_view(), name='order_update'),
    path('order/<int:pk>/delete/', OrderDeleteView.as_view(), name='order_delete'),

    # Pharmacist URLs
    path('pharmacists/', PharmacistListView.as_view(), name='pharmacist_list'),
    path('pharmacist/<int:pk>/', PharmacistDetailView.as_view(), name='pharmacist_detail'),
    path('pharmacist/new/', PharmacistCreateView.as_view(), name='pharmacist_create'),
    path('pharmacist/<int:pk>/edit/', PharmacistUpdateView.as_view(), name='pharmacist_update'),
    path('pharmacist/<int:pk>/delete/', PharmacistDeleteView.as_view(), name='pharmacist_delete'),
]
