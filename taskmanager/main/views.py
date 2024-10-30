from django.shortcuts import render, redirect, get_object_or_404
from .models import Client, Medicine, Supplier,  Order, Pharmacist, Prescription, PrescriptionMedicine
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_detail.html', {'client': client})

def client_create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        date_of_birth = request.POST.get('date_of_birth')
        gender = request.POST.get('gender')

        if not all([name, surname, phone, email]):
            return HttpResponse("All fields are required", status=400)

        client = Client(
            name=name, 
            surname=surname, 
            phone=phone, 
            email=email, 
            date_of_birth=date_of_birth, 
            gender=gender
        )
        client.save()
        return redirect('client_list')
    return render(request, 'client_form.html')

def client_update(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == "POST":
        client.name = request.POST.get('name')
        client.surname = request.POST.get('surname')
        client.phone = request.POST.get('phone')
        client.email = request.POST.get('email')
        client.date_of_birth = request.POST.get('date_of_birth')
        client.gender = request.POST.get('gender')
        client.save()
        return redirect('client_list')
    return render(request, 'client_form.html', {'client': client})

def client_delete(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    client.delete()
    return redirect('client_list')

def supplier_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

def supplier_detail(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    return render(request, 'supplier_detail.html', {'supplier': supplier})

def supplier_create(request):
    if request.method == 'POST':
        company_name = request.POST['company_name']
        phone = request.POST['phone']
        email = request.POST['email']
        Supplier.objects.create(company_name=company_name, phone=phone, email=email)
        return redirect('supplier_list')
    return render(request, 'supplier_form.html')

def supplier_update(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == 'POST':
        supplier.company_name = request.POST['company_name']
        supplier.phone = request.POST['phone']
        supplier.email = request.POST['email']
        supplier.save()
        return redirect('supplier_list')
    return render(request, 'supplier_form.html', {'supplier': supplier})

def supplier_delete(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'supplier_confirm_delete.html', {'supplier': supplier})

from django.shortcuts import render
from .models import Supplier

def supplier_list(request):
    search_id = request.GET.get('search_id', None)
    if search_id:
        suppliers = Supplier.objects.filter(id=search_id)
    else:
        suppliers = Supplier.objects.all()
    
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

def medicine_list(request):
    medicines = Medicine.objects.all()
    return render(request, 'medicine_list.html', {'medicines': medicines})

def medicine_detail(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    return render(request, 'medicine_detail.html', {'medicine': medicine})

def medicine_create(request):
    if request.method == "POST":
        medicine_name = request.POST.get('medicine_name')
        storage = request.POST.get('storage')
        supplier_name = request.POST.get('supplier_name')
        delivery_date = request.POST.get('delivery_date')
        quantity = request.POST.get('quantity')
        price = request.POST.get('price')
        dosage_form = request.POST.get('dosage_form')

        if not all([medicine_name, storage, supplier_name, delivery_date, quantity, price, dosage_form]):
            return HttpResponse("All fields are required", status=400)

        medicine = Medicine(
            Medicine_Name=medicine_name,
            Storage=storage,
            SupplierName=supplier_name,
            DeliveryDate=delivery_date,
            Quantity=quantity,
            Price=price,
            DosageForm=dosage_form
        )
        medicine.save()
        return redirect('medicine_list')
    return render(request, 'medicine_form.html')

def medicine_update(request, medicine_id):
    medicine = get_object_or_404(Medicine, id=medicine_id)
    if request.method == "POST":
        medicine.Medicine_Name = request.POST.get('medicine_name')
        medicine.Storage = request.POST.get('storage')
        medicine.SupplierName = request.POST.get('supplier_name')
        medicine.DeliveryDate = request.POST.get('delivery_date')
        medicine.Quantity = request.POST.get('quantity')
        medicine.Price = request.POST.get('price')
        medicine.DosageForm = request.POST.get('dosage_form')
        medicine.save()
        return redirect('medicine_list')
    return render(request, 'medicine_form.html', {'medicine': medicine})

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

def order_list(request):
    search_id = request.GET.get('search_id')  
    if search_id:
        orders = Order.objects.filter(id=search_id)  
    else:
        orders = Order.objects.all()  
    
    return render(request, 'order_list.html', {'orders': orders})

def order_create(request):
    if request.method == 'POST':
        date = request.POST['date']
        total_price = request.POST['total_price']
        payment_method = request.POST['payment_method']
        pharmacist_id = request.POST['pharmacist_id']
        client_id = request.POST['client_id']
        Order.objects.create(
            date=date,
            total_price=total_price,
            payment_method=payment_method,
            pharmacist_id=pharmacist_id,
            client_id=client_id
        )
        return redirect('order_list')
    return render(request, 'order_form.html')

def order_update(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.date = request.POST['date']
        order.total_price = request.POST['total_price']
        order.payment_method = request.POST['payment_method']
        order.pharmacist_id = request.POST['pharmacist_id']
        order.client_id = request.POST['client_id']
        order.save()
        return redirect('order_list')
    return render(request, 'order_form.html', {'order': order})

def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'order_detail.html', {'order': order})

def order_delete(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order_confirm_delete.html', {'order': order})


def pharmacist_create(request):
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_surname = request.POST['client_surname']
        start_date = request.POST['start_date']
        end_date = request.POST.get('end_date')
        notes = request.POST.get('notes')

        client = Client.objects.create(name=client_name, surname=client_surname)
        Pharmacist.objects.create(client=client, start_date=start_date, end_date=end_date, notes=notes)
        return redirect('pharmacist_list')

    return render(request, 'pharmacist_form.html')

def pharmacist_update(request, pharmacist_id):
    pharmacist = get_object_or_404(Pharmacist, id=pharmacist_id)
    if request.method == 'POST':
        pharmacist.client.name = request.POST['client_name']
        pharmacist.client.surname = request.POST['client_surname']
        pharmacist.start_date = request.POST['start_date']
        pharmacist.end_date = request.POST.get('end_date')
        pharmacist.notes = request.POST.get('notes')
        pharmacist.client.save()
        pharmacist.save()
        return redirect('pharmacist_list')

    return render(request, 'pharmacist_form.html', {'pharmacist': pharmacist})

def pharmacist_detail(request, pharmacist_id):
    pharmacist = get_object_or_404(Pharmacist, id=pharmacist_id)
    return render(request, 'pharmacist_detail.html', {'pharmacist': pharmacist})

def pharmacist_delete(request, pharmacist_id):
    pharmacist = get_object_or_404(Pharmacist, id=pharmacist_id)
    pharmacist.delete()
    return redirect('pharmacist_list')

def pharmacist_list(request):
    pharmacists = Pharmacist.objects.all()
    return render(request, 'pharmacist_list.html', {'pharmacists': pharmacists})

def prescription_create(request):
    if request.method == 'POST':
        pharmacist_id = request.POST['pharmacist_id']
        client_id = request.POST['client_id']
        date = request.POST['date']
        notes = request.POST.get('notes')

        prescription = Prescription.objects.create(
            pharmacist_id=pharmacist_id,
            client_id=client_id,
            date=date,
            notes=notes
        )
        
        medicine_ids = request.POST.getlist('medicine_ids')
        for medicine_id in medicine_ids:
            PrescriptionMedicine.objects.create(prescription=prescription, medicine_id=medicine_id)
        
        return redirect('prescription_list')

    return render(request, 'prescription_form.html')

def prescription_update(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    if request.method == 'POST':
        prescription.date = request.POST['date']
        prescription.notes = request.POST.get('notes')
        prescription.save()        
        return redirect('prescription_list')

    return render(request, 'prescription_form.html', {'prescription': prescription})

def prescription_detail(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    medicines = PrescriptionMedicine.objects.filter(prescription=prescription)
    return render(request, 'prescription_detail.html', {'prescription': prescription, 'medicines': medicines})

def prescription_delete(request, prescription_id):
    prescription = get_object_or_404(Prescription, id=prescription_id)
    prescription.delete()
    return redirect('prescription_list')

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescription_list.html', {'prescriptions': prescriptions})