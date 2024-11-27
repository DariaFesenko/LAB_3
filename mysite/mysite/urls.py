from django.contrib import admin
from django.urls import path, include
from .views import agent_list, client_list
from rest_framework.routers import DefaultRouter
from mysite.views import (
    api_agent_view,
    OrderViewSet,
    MedicineViewSet,
    ClientViewSet,
    PrescriptionViewSet,
    SupplierViewSet,
    PharmacistViewSet,

)

router = DefaultRouter()
router.register(r'medicines', MedicineViewSet, basename='medicine')
router.register(r'suppliers', SupplierViewSet, basename='supplier')
router.register(r'prescriptions', PrescriptionViewSet, basename='prescription')
#router.register(r'clients', ClientViewSet, basename='client')
router.register(r'orders', OrderViewSet, basename='order')
router.register(r'pharmacists', PharmacistViewSet, basename='pharmacist')




urlpatterns = [
    path('admin/', admin.site.urls),
    path('pharmacy/', include('pharmacy.urls')),
    #path("agents/", agent_list, name="agent_list"),
    #path("clients/", client_list, name="client_list"),
    path('', include('pharmacy.urls')),
    #path('api-auth/', include('rest_framework.urls')),
    path('clients/', include('pharmacy.urls')),
    path('', include(router.urls)),
    #path('api/agents/', api_agent_view, name='api_agents')
]