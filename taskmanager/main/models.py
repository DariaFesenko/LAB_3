from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    phone = models.BigIntegerField()
    email = models.EmailField()
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"
    
class Supplier(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.company_name


class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    medicine_name = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='medicines')
    delivery_date = models.DateField()
    quantity = models.IntegerField()
    price = models.FloatField()
    dosage_form = models.CharField(max_length=255)

    def __str__(self):
        return self.medicine_name
    
class Client(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)

class Pharmacist(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE)

class Order(models.Model):
    date = models.DateField()
    total_price = models.FloatField()
    payment_method = models.CharField(max_length=255)
    pharmacist = models.ForeignKey(Pharmacist, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Prescription(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    notes = models.CharField(max_length=255, null=True, blank=True)

class PrescriptionMedicine(models.Model):
    prescription = models.ForeignKey(Prescription, on_delete=models.CASCADE)
    medicine_id = models.IntegerField() 