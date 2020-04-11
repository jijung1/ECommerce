from django.db import models

class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    supplierId = models.IntegerField()
    price = models.DecimalField(max_digits=20, decimal_places=2)
    stock_qty = models.IntegerField()

    def __str__(self):
        return 'PId: ' + str(self.id) + ', Name: ' + self.prod_name + ', Supplier: ' + str(self.supplierId) + ', Qty: ' + str(self.stock_qty) + ', Price: $' + str(self.price)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    ship_street = models.CharField(max_length=50)
    ship_city = models.CharField(max_length=50)
    ship_state = models.CharField(max_length=50)
    ship_country = models.CharField(max_length=50)

    def __str__(self):
        return 'Name: ' + self.first_name + ' ' + self.last_name


class Supplier(models.Model):
    supplier_name = models.CharField(max_length=50)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return 'Supplier: ' + self.supplier_name + ' product: ' + self.product_name + ' supplier price: ' + self.price


class Order(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    supplier_id = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    tracking_number = models.CharField(max_length=50)
    customer_rating = models.DecimalField(max_digits=1, decimal_places=1)
    bill_street = models.CharField(max_length=50)
    bill_city = models.CharField(max_length=50)
    bill_state = models.CharField(max_length=50)
    bill_country = models.CharField(max_length=50)
    bill_postal_code = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return 'CustomerId: ' + self.customer_id + ' productId: ' + self.product_id + ' quantity: ' + self.quantity + ' Total: ' + self.total


