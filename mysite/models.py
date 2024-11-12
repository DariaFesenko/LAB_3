from django.db import models

class Supplier(models.Model):
    company_name = models.CharField(max_length=255, null=False, unique=True)  
    phone_number = models.CharField(max_length=15, null=False)  
    email = models.EmailField(null=True, blank=True)  
    address = models.CharField(max_length=255, null=False) 

    def __str__(self):
        return self.company_name
    
class Medicine(models.Model):
    name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE) 
    price = models.DecimalField(max_digits=10, decimal_places=2, null=False)  
    description = models.TextField(null=True, blank=True) 

    def __str__(self):
        return self.name

class Client(models.Model):
    first_name = models.CharField(max_length=100, null=False)  
    last_name = models.CharField(max_length=100, null=False) 
    phone_number = models.CharField(max_length=15, null=False) 
    email = models.EmailField(null=True, blank=True)
    gender = models.CharField(max_length=255, null=False)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Prescription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE) 
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE)  
    quantity = models.IntegerField(null=False) 
    date_issued = models.DateField(null=False)  

    def __str__(self):
        return f"Prescription for {self.client} - {self.medicine}"

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE) 
    medicine = models.ForeignKey(Medicine, on_delete=models.CASCADE) 
    quantity = models.IntegerField(null=False)  
    order_date = models.DateField(null=False) 
    status = models.CharField(max_length=50, null=False) 

    def __str__(self):
        return f"Order for {self.client} - {self.medicine}"

class Pharmacist(models.Model):
    first_name = models.CharField(max_length=100, null=False) 
    last_name = models.CharField(max_length=100, null=False) 
    phone_number = models.CharField(max_length=15, null=False)  
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
