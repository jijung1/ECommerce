from django.db import models
from phone_field import PhoneField


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return 'Supplier: ' + self.supplier_name + ' product: ' + self.product_name + ' supplier price: ' + str(self.price)


class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    units_in_stock = models.IntegerField()
    units_on_order = models.IntegerField()
    supplier_id = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'PId: ' + str(self.id) + ', Name: ' + self.prod_name + ', Supplier: ' + str(self.supplier_id) + ', Qty: ' + str(self.units_in_stock) + ', Price: $' + str(self.price)


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    ship_street = models.CharField(max_length=50)
    ship_city = models.CharField(max_length=50)
    ship_state = models.CharField(max_length=50)
    ship_country = models.CharField(max_length=50)
    assigned_employee = models.ForeignKey(Employee, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return 'Name: ' + self.first_name + ' ' + self.last_name


class Shipper(models.Model):
    shipper_name = models.CharField(max_length=64)
    phone = PhoneField(blank=True)


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product_id = models.ManyToManyField(Product)
    ship_via = models.ForeignKey(Shipper, on_delete=models.DO_NOTHING)
    tracking_number = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    customer_rating = models.DecimalField(max_digits=2, decimal_places=1)
    bill_street = models.CharField(max_length=50)
    bill_city = models.CharField(max_length=50)
    bill_state = models.CharField(max_length=50)
    bill_country = models.CharField(max_length=50)
    bill_postal_code = models.CharField(max_length=50)
    invoice_total = models.DecimalField(max_digits=20, decimal_places=2)
    date_ordered = models.DateTimeField()
    date_shipped = models.DateTimeField()
    date_completed = models.DateTimeField()

    def __str__(self):
        return 'CustomerId: ' + str(self.customer_id) + ' productId: ' + str(self.product_id) +\
               ' Total: ' + str(self.invoice_total)



