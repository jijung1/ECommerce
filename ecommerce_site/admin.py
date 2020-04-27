from django.contrib import admin
from .models import Product, Customer, Order, Supplier, Employee, Shipper

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Supplier)
admin.site.register(Employee)
admin.site.register(Shipper)