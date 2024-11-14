from .models import Medicine, Client, Supplier, Prescription, Pharmacist, Order
from django.db.models import Avg, Sum, Count

class MedicineRepository:
    @staticmethod
    def get_all_medicines():
        return Medicine.objects.all()

    @staticmethod
    def get_medicine_by_id(medicine_id):
        try:
            return Medicine.objects.get(id=medicine_id)
        except Medicine.DoesNotExist:
            return None

    @staticmethod
    def create_medicine(data):
        return Medicine.objects.create(**data)

    @staticmethod
    def update_medicine(medicine_id, data):
        medicine = MedicineRepository.get_medicine_by_id(medicine_id)
        if medicine:
            for key, value in data.items():
                setattr(medicine, key, value)
            medicine.save()
            return medicine
        return None

    @staticmethod
    def delete_medicine(medicine_id):
        medicine = MedicineRepository.get_medicine_by_id(medicine_id)
        if medicine:
            medicine.delete()
            return True
        return False

    @staticmethod
    def get_aggregated_data():
        return Medicine.objects.aggregate(total_price=Sum('price'), average_price=Avg('price'))
    

class MedicineRepository:
    @staticmethod
    def get_all_medicines():
        return Medicine.objects.all()

    @staticmethod
    def get_medicine_by_id(medicine_id):
        try:
            return Medicine.objects.get(id=medicine_id)
        except Medicine.DoesNotExist:
            return None

    @staticmethod
    def create_medicine(data):
        return Medicine.objects.create(**data)

    @staticmethod
    def update_medicine(medicine_id, data):
        medicine = MedicineRepository.get_medicine_by_id(medicine_id)
        if medicine:
            for key, value in data.items():
                setattr(medicine, key, value)
            medicine.save()
            return medicine
        return None

    @staticmethod
    def delete_medicine(medicine_id):
        medicine = MedicineRepository.get_medicine_by_id(medicine_id)
        if medicine:
            medicine.delete()
            return True
        return False

    @staticmethod
    def get_aggregated_data():
        return Medicine.objects.aggregate(total_price=Sum('price'), average_price=Avg('price'))


class ClientRepository:
    @staticmethod
    def get_all_clients():
        return Client.objects.all()

    @staticmethod
    def get_client_by_id(client_id):
        try:
            return Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return None

    @staticmethod
    def create_client(data):
        return Client.objects.create(**data)

    @staticmethod
    def update_client(client_id, data):
        client = ClientRepository.get_client_by_id(client_id)
        if client:
            for key, value in data.items():
                setattr(client, key, value)
            client.save()
            return client
        return None

    @staticmethod
    def delete_client(client_id):
        client = ClientRepository.get_client_by_id(client_id)
        if client:
            client.delete()
            return True
        return False

    @staticmethod
    def get_client_summary():
        return Client.objects.aggregate(
            total_clients=Count('id')
        )
        
class MedicineRepository:
    @staticmethod
    def get_all_medicines():
        return Medicine.objects.all()

    @staticmethod
    def get_medicine_by_id(medicine_id):
        try:
            return Medicine.objects.get(id=medicine_id)
        except Medicine.DoesNotExist:
            return None

    @staticmethod
    def create_medicine(data):
        return Medicine.objects.create(**data)

    @staticmethod
    def update_medicine(medicine_id, data):
        medicine = MedicineRepository.get_medicine_by_id(medicine_id)
        if medicine:
            for key, value in data.items():
                setattr(medicine, key, value)
            medicine.save()
            return medicine
        return None

    @staticmethod
    def delete_medicine(medicine_id):
        medicine = MedicineRepository.get_medicine_by_id(medicine_id)
        if medicine:
            medicine.delete()
            return True
        return False

    @staticmethod
    def get_aggregated_data():
        return Medicine.objects.aggregate(total_price=Sum('price'), average_price=Avg('price'))


class ClientRepository:
    @staticmethod
    def get_all_clients():
        return Client.objects.all()

    @staticmethod
    def get_client_by_id(client_id):
        try:
            return Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return None

    @staticmethod
    def create_client(data):
        return Client.objects.create(**data)

    @staticmethod
    def update_client(client_id, data):
        client = ClientRepository.get_client_by_id(client_id)
        if client:
            for key, value in data.items():
                setattr(client, key, value)
            client.save()
            return client
        return None

    @staticmethod
    def delete_client(client_id):
        client = ClientRepository.get_client_by_id(client_id)
        if client:
            client.delete()
            return True
        return False

    @staticmethod
    def get_client_summary():
        return Client.objects.aggregate(total_clients=Count('id'))


class SupplierRepository:
    @staticmethod
    def get_all_suppliers():
        return Supplier.objects.all()

    @staticmethod
    def get_supplier_by_id(supplier_id):
        try:
            return Supplier.objects.get(id=supplier_id)
        except Supplier.DoesNotExist:
            return None

    @staticmethod
    def create_supplier(data):
        return Supplier.objects.create(**data)

    @staticmethod
    def update_supplier(supplier_id, data):
        supplier = SupplierRepository.get_supplier_by_id(supplier_id)
        if supplier:
            for key, value in data.items():
                setattr(supplier, key, value)
            supplier.save()
            return supplier
        return None

    @staticmethod
    def delete_supplier(supplier_id):
        supplier = SupplierRepository.get_supplier_by_id(supplier_id)
        if supplier:
            supplier.delete()
            return True
        return False

    @staticmethod
    def get_supplier_summary():
        return Supplier.objects.aggregate(total_suppliers=Count('id'))
    
class MedicineRepository:
    @staticmethod
    def get_all_medicines():
        return Medicine.objects.all()

    @staticmethod
    def get_medicine_by_id(medicine_id):
        try:
            return Medicine.objects.get(id=medicine_id)
        except Medicine.DoesNotExist:
            return None

    @staticmethod
    def create_medicine(data):
        return Medicine.objects.create(**data)

    @staticmethod
    def update_medicine(medicine_id, data):
        medicine = MedicineRepository.get_medicine_by_id(medicine_id)
        if medicine:
            for key, value in data.items():
                setattr(medicine, key, value)
            medicine.save()
            return medicine
        return None

    @staticmethod
    def delete_medicine(medicine_id):
        medicine = MedicineRepository.get_medicine_by_id(medicine_id)
        if medicine:
            medicine.delete()
            return True
        return False

    @staticmethod
    def get_aggregated_data():
        return Medicine.objects.aggregate(total_price=Sum('price'), average_price=Avg('price'))


class ClientRepository:
    @staticmethod
    def get_all_clients():
        return Client.objects.all()

    @staticmethod
    def get_client_by_id(client_id):
        try:
            return Client.objects.get(id=client_id)
        except Client.DoesNotExist:
            return None

    @staticmethod
    def create_client(data):
        return Client.objects.create(**data)

    @staticmethod
    def update_client(client_id, data):
        client = ClientRepository.get_client_by_id(client_id)
        if client:
            for key, value in data.items():
                setattr(client, key, value)
            client.save()
            return client
        return None

    @staticmethod
    def delete_client(client_id):
        client = ClientRepository.get_client_by_id(client_id)
        if client:
            client.delete()
            return True
        return False

    @staticmethod
    def get_client_summary():
        return Client.objects.aggregate(total_clients=Count('id'))


class SupplierRepository:
    @staticmethod
    def get_all_suppliers():
        return Supplier.objects.all()

    @staticmethod
    def get_supplier_by_id(supplier_id):
        try:
            return Supplier.objects.get(id=supplier_id)
        except Supplier.DoesNotExist:
            return None

    @staticmethod
    def create_supplier(data):
        return Supplier.objects.create(**data)

    @staticmethod
    def update_supplier(supplier_id, data):
        supplier = SupplierRepository.get_supplier_by_id(supplier_id)
        if supplier:
            for key, value in data.items():
                setattr(supplier, key, value)
            supplier.save()
            return supplier
        return None

    @staticmethod
    def delete_supplier(supplier_id):
        supplier = SupplierRepository.get_supplier_by_id(supplier_id)
        if supplier:
            supplier.delete()
            return True
        return False

    @staticmethod
    def get_supplier_summary():
        return Supplier.objects.aggregate(total_suppliers=Count('id'))


class PrescriptionRepository:
    @staticmethod
    def get_all_prescriptions():
        return Prescription.objects.all()

    @staticmethod
    def get_prescription_by_id(prescription_id):
        try:
            return Prescription.objects.get(id=prescription_id)
        except Prescription.DoesNotExist:
            return None

    @staticmethod
    def create_prescription(data):
        return Prescription.objects.create(**data)

    @staticmethod
    def update_prescription(prescription_id, data):
        prescription = PrescriptionRepository.get_prescription_by_id(prescription_id)
        if prescription:
            for key, value in data.items():
                setattr(prescription, key, value)
            prescription.save()
            return prescription
        return None

    @staticmethod
    def delete_prescription(prescription_id):
        prescription = PrescriptionRepository.get_prescription_by_id(prescription_id)
        if prescription:
            prescription.delete()
            return True
        return False

    @staticmethod
    def get_prescription_summary():
        return Prescription.objects.aggregate(
            total_prescriptions=Count('id'),
            total_quantity=Sum('quantity')
        )
        
class PharmacistRepository:
    @staticmethod
    def get_all_pharmacists():
        return Pharmacist.objects.all()

    @staticmethod
    def get_pharmacist_by_id(pharmacist_id):
        try:
            return Pharmacist.objects.get(id=pharmacist_id)
        except Pharmacist.DoesNotExist:
            return None

    @staticmethod
    def create_pharmacist(data):
        return Pharmacist.objects.create(**data)

    @staticmethod
    def update_pharmacist(pharmacist_id, data):
        pharmacist = PharmacistRepository.get_pharmacist_by_id(pharmacist_id)
        if pharmacist:
            for key, value in data.items():
                setattr(pharmacist, key, value)
            pharmacist.save()
            return pharmacist
        return None

    @staticmethod
    def delete_pharmacist(pharmacist_id):
        pharmacist = PharmacistRepository.get_pharmacist_by_id(pharmacist_id)
        if pharmacist:
            pharmacist.delete()
            return True
        return False

    @staticmethod
    def get_pharmacist_summary():
        return Pharmacist.objects.aggregate(total_pharmacists=Count('id'))
    
class OrderRepository:
    @staticmethod
    def get_all_orders():
        return Order.objects.all()

    @staticmethod
    def get_order_by_id(order_id):
        try:
            return Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return None

    @staticmethod
    def create_order(data):
        return Order.objects.create(**data)

    @staticmethod
    def update_order(order_id, data):
        order = OrderRepository.get_order_by_id(order_id)
        if order:
            for key, value in data.items():
                setattr(order, key, value)
            order.save()
            return order
        return None

    @staticmethod
    def delete_order(order_id):
        order = OrderRepository.get_order_by_id(order_id)
        if order:
            order.delete()
            return True
        return False

    @staticmethod
    def get_order_summary():
        return Order.objects.aggregate(
            total_orders=Count('id'),
            total_quantity=Sum('quantity')
        )