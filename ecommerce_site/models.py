from django.db import models


class Product(models.Model):
    prod_name = models.CharField(max_length=100)
    supplier = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    stock_qty = models.IntegerField()
    def __str__(self):
        return self.prod_name + ' - ' + str(self.price)

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    last_purchased_prod = models.ForeignKey(Product, on_delete=models.CASCADE)
