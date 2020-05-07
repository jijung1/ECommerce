from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
# from django.template import loader #there's a short cut using shortcuts
from .models import *
from django.contrib.auth.decorators import login_required
from .filters import *
from django.http import JsonResponse
from django.views.generic import View
from rest_framework.views import APIView
from rest_framework.response import Response

# mysql connection for raw sql queries
import mysql.connector
from mysql.connector import Error
import pandas as pd

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mysql.connector.connect(host='34.83.244.203',
                                       database='ecommerce',
                                       user='user1',
                                       password='spring2020cpsc408')
        if conn.is_connected():
            print('Connected to MySQL database')
            return conn
    except Error as e:
        print(e)


def loginpage(request):
    if request.user.is_authenticated:
        print("user still authenticated")
        return render(request, 'ecommerce_site/main.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'ecommerce_site/main.html')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'ecommerce_site/login.html')
    print("rendering login page")
    return render(request, 'ecommerce_site/login.html')


@login_required(login_url='loginpage')
def mainpage(request):

    #using queryset
    products = Product.objects.all()
    orders = Order.objects.all()
    shippers = Shipper.objects.all()
    customers = Customer.objects.all()
    employees = Employee.objects.all()
    print("mainpage function called")

    context = {
        'products': products,
        'orders': orders,
        'shippers': shippers,
        'customers': customers,
        'employees': employees
    }
    return render(request, 'ecommerce_site/main.html', context)


@login_required(login_url='loginpage')
def querypage(request):

    #using queryset
    products = Product.objects.all()
    orders = Order.objects.all()
    shippers = Shipper.objects.all()
    customers = Customer.objects.all()
    employees = Employee.objects.all()
    suppliers = Supplier.objects.all()

    #render data, filter, and remake variable with filtered down data
    productFilter = ProductFilter(request.POST, queryset=products)
    products = productFilter.qs

    orderFilter = OrderFilter(request.POST, queryset=orders)
    orders = orderFilter.qs

    context = {
        'products': products,
        'orders': orders,
        'shippers': shippers,
        'customers': customers,
        'employees': employees,
        'suppliers': suppliers,
        'orderFilter': orderFilter,
        'productFilter': productFilter
    }
    return render(request, 'ecommerce_site/query.html', context)

@login_required(login_url='loginpage')
def logoutpage(request):
    print("logout requestsed")
    logout(request)
    print("logout processed")
    return redirect('loginpage')

@login_required(login_url='loginpage')
class MainView(View):
    def get(self, request, *args, **kwargs):
        print("mainView function called")
        return render(request, 'main.html')



"""
def get_data(request, *args, **kwargs):
    data = {
        "data": [65, 59, 80, 81, 56, 55, 40],
        "data2": [10, 20, 30, 40, 50, 60, 70]
    }
    return JsonResponse(data) #http response
"""

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        conn = connect()
        cursor = conn.cursor()

        cursor.execute('SELECT ecommerce_site_employee.first_name, ecommerce_site_employee.last_name, AVG(customer_rating) employee_average_rating FROM ecommerce_site_employee JOIN ecommerce_site_customer ON ecommerce_site_employee.id = ecommerce_site_customer.assigned_employee_id JOIN ecommerce_site_order on ecommerce_site_customer.id = ecommerce_site_order.customer_id_id GROUP BY ecommerce_site_employee.id ORDER BY 3 desc limit 5')
        best_rated_employee = cursor.fetchall()
        cursor.execute('SELECT ecommerce_site_employee.first_name, ecommerce_site_employee.last_name, SUM(invoice_total) FROM ecommerce_site_employee JOIN ecommerce_site_customer ON ecommerce_site_employee.id = ecommerce_site_customer.assigned_employee_id JOIN ecommerce_site_order on ecommerce_site_customer.id = ecommerce_site_order.customer_id_id GROUP BY ecommerce_site_employee.id ORDER BY 3 desc limit 5')
        best_sale_employee = cursor.fetchall()

        cursor.execute("SELECT SUM(invoice_total) FROM ecommerce_site_order WHERE date_completed BETWEEN '2020-05-01' AND '2020-05-31'")
        month_revenue_may = cursor.fetchall()
        cursor.execute("SELECT SUM(invoice_total) FROM ecommerce_site_order WHERE date_completed BETWEEN '2020-04-01' AND '2020-04-30'")
        month_revenue_april = cursor.fetchall()
        cursor.execute("SELECT SUM(invoice_total) FROM ecommerce_site_order WHERE date_completed BETWEEN '2020-03-01' AND '2020-03-31'")
        month_revenue_march = cursor.fetchall()



        print("ChartData function called")
        print(type(best_rated_employee))

        data = {
            "employee_rating": best_rated_employee,
            "employee_sales": best_sale_employee,
            "month_revenue_may": month_revenue_may,
            "month_revenue_april": month_revenue_april,
            "month_revenue_march": month_revenue_march
        }
        return Response(data)








