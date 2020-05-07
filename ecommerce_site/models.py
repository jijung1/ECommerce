from django.db import models
from phone_field import PhoneField


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['supplier_name', 'product_name', 'price'])
        ]

    def __str__(self):
        return '||Supplier name||: ' + self.supplier_name \
                + ' ||Product||: ' + self.product_name + ' ||Supplier Price||: ' + str(self.price)


class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    units_in_stock = models.IntegerField()
    units_on_order = models.IntegerField()
    supplier_id = models.ForeignKey(Supplier, null=True, on_delete=models.SET_NULL)

    class Meta:
        indexes = [
            models.Index(fields=['prod_name', 'price', 'units_in_stock', 'units_on_order'])
        ]

    def __str__(self):
        return '||Product name||: ' + self.prod_name + ' ||Price||: ' + str(self.price) + ' ||Units in stock||: ' + \
               str(self.units_in_stock) + ' ||Units on order||: ' + str(self.units_on_order) + ' ||Supplier||: ' + self.supplier_id.supplier_name


class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return '||Employee name||: ' + self.first_name + ' ' + self.last_name + ' ||Title||: ' \
               + self.title + ' ||Email||: ' + self.email


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

    class Meta:
        indexes = [
            models.Index(fields=['first_name', 'last_name', 'company', 'email', 'ship_street', 'ship_city',
                                 'ship_state', 'ship_country', 'assigned_employee'])
        ]
    def __str__(self):
        return '||Name||: ' + self.first_name + ' ' + self.last_name + ' ||Company||: ' + self.company +\
               ' ||Email||: ' + self.email + ' ||Shipping Address||: ' + self.ship_street + ' ' +\
               self.ship_city + ' ' + self.ship_state + ' ' + self.ship_country


class Shipper(models.Model):
    shipper_name = models.CharField(max_length=64)
    phone = PhoneField(blank=True)

    def __str__(self):
        return '||Shipper||: ' + self.shipper_name + ' ||Phone||: ' + str(self.phone)


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
    date_completed = models.DateTimeField(null=True)

    class Meta:
        indexes = [
            models.Index(fields=['invoice_total', 'customer_id', 'ship_via', 'tracking_number',
                                 'status', 'customer_rating', 'date_ordered', 'date_shipped', 'date_completed'])
        ]

    def __str__(self):
        return '||CustomerId||: ' + str(self.customer_id) + ' ||productId||: ' + str(self.product_id) +\
               ' ||Total||: ' + str(self.invoice_total)



