from django.db import models
from django.urls import reverse


# Create your models here.
# pharmasy/models.py

from django.db import models


class Supplier(models.Model):
    company_name = models.CharField(max_length=255, null=False, unique=True)  
    phone_number = models.CharField(max_length=15, null=False)  
    email = models.EmailField(null=True, blank=True)  
    address = models.CharField(max_length=255, null=False) 

    def __str__(self):
        return self.company_name
    
    
class Client(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    phone_number = models.CharField(max_length=15, null=False)
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=255, null=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def get_absolute_url(self):
        return reverse('pharmacy:client_detail', args=[str(self.id)]) 
    
