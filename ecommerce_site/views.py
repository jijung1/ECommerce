from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
#from django.template import loader #there's a short cut using shortcuts
from .models import Product


def index(request):
    all_products = Product.objects.raw('SELECT id,prod_name, supplier, price FROM ecommerce_site_product WHERE price < 50.99 ')
    return render(request, 'product/index.html', {'all_products' : all_products})


def detail(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
    except Product.DoesNotExist:
        raise Http404("Product does not exist")
    return render(request, 'product/detail.html', {'product': product})
