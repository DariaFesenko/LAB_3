from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from mysite import views
from mysite.views import MedicineViewSet, ClientViewSet, PrescriptionViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r'medicine', MedicineViewSet)
router.register(r'client', ClientViewSet)
router.register(r'prescription', PrescriptionViewSet)
router.register(r'supplier', SupplierViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)), 
    path('home/', views.home, name='home'),
    ]
