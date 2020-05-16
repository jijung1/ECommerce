from django.forms import ModelForm
from .models import *


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class ShipperForm(ModelForm):
    class Meta:
        model = Shipper
        fields = '__all__'



