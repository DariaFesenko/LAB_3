from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home')
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'prescriptions', views.PrescriptionViewSet)
router.register(r'clients', views.ClientViewSet)
urlpatterns = [
    path('', include(router.urls)),
]