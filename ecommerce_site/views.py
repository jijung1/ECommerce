import csv
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
# from django.template import loader #there's a short cut using shortcuts
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
from .forms import *

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
        return redirect('mainpage')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('mainpage')
        else:
            messages.info(request, 'Username OR Password is incorrect')
            return render(request, 'ecommerce_site/login.html')
    print("rendering login page")
    return render(request, 'ecommerce_site/login.html')

@login_required(login_url='loginpage')
def mainpage(request):
    return render(request, 'ecommerce_site/main.html')

@login_required(login_url='loginpage')
def query_order(request):
    orders = Order.objects.all()
    orderFilter = OrderFilter(request.POST, queryset=orders)
    orders = orderFilter.qs

    context = {
        'orders': orders,
        'orderFilter': orderFilter,
    }
    return render(request, 'ecommerce_site/orders.html', context)

@login_required(login_url='loginpage')
def query_supplier(request):
    suppliers = Supplier.objects.all()
    # TODO: add parameterized filters to filters.py
    # supplierFilter = SupplierFilter(request.POST, queryset=suppliers)
    # suppliers = supplierFilter.qs

    context = {
        'suppliers': suppliers,
        # 'supplierFilter': supplierFilter,
    }
    return render(request, 'ecommerce_site/suppliers.html', context)


@login_required(login_url='loginpage')
def query_product(request):
    products = Product.objects.all()
    productFilter = ProductFilter(request.POST, queryset=products)
    products = productFilter.qs

    context = {
        'products': products,
        'productFilter': productFilter,
    }
    return render(request, 'ecommerce_site/products.html', context)

@login_required(login_url='loginpage')
def query_employee(request):
    employees = Employee.objects.all()
    # employeeFilter = EmployeeFilter(request.POST, queryset=products)
    #employees = employeeFilter.qs

    context = {
        'employees': employees,
       # 'employeeFilter': employeeFilter,
    }
    return render(request, 'ecommerce_site/employees.html', context)

@login_required(login_url='loginpage')
def query_customer(request):
    customers = Customer.objects.all()
    # customerFilter = CustomerFilter(request.POST, queryset=products)
    #customers = customerFilter.qs

    context = {
        'customers': customers,
       # 'customerFilter': customerFilter,
    }
    return render(request, 'ecommerce_site/customers.html', context)

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

"""
@login_required(login_url='loginpage')
class MainView(View):
    def get(self, request, *args, **kwargs):
        print("mainView function called")
        return render(request, 'ecommerce_site/main.html')"""


@login_required(login_url='loginpage')
def generate_report(request):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        'SELECT ecommerce_site_employee.first_name, ecommerce_site_employee.last_name, AVG(customer_rating) employee_average_rating FROM ecommerce_site_employee JOIN ecommerce_site_customer ON ecommerce_site_employee.id = ecommerce_site_customer.assigned_employee_id JOIN ecommerce_site_order on ecommerce_site_customer.id = ecommerce_site_order.customer_id_id GROUP BY ecommerce_site_employee.id ORDER BY 3 desc limit 5')
    best_rated_employee = cursor.fetchall()
    cursor.execute(
        'SELECT ecommerce_site_employee.first_name, ecommerce_site_employee.last_name, SUM(invoice_total) FROM ecommerce_site_employee JOIN ecommerce_site_customer ON ecommerce_site_employee.id = ecommerce_site_customer.assigned_employee_id JOIN ecommerce_site_order on ecommerce_site_customer.id = ecommerce_site_order.customer_id_id GROUP BY ecommerce_site_employee.id ORDER BY 3 desc limit 5')
    best_sale_employee = cursor.fetchall()
    cursor.execute(
        "SELECT SUM(invoice_total) FROM ecommerce_site_order WHERE date_completed BETWEEN '2020-05-01' AND '2020-05-31'")
    month_revenue_may = cursor.fetchall()
    cursor.execute(
        "SELECT SUM(invoice_total) FROM ecommerce_site_order WHERE date_completed BETWEEN '2020-04-01' AND '2020-04-30'")
    month_revenue_april = cursor.fetchall()
    cursor.execute(
        "SELECT SUM(invoice_total) FROM ecommerce_site_order WHERE date_completed BETWEEN '2020-03-01' AND '2020-03-31'")
    month_revenue_march = cursor.fetchall()

    conn.close()

    """
        context = {'best_rated_employee': best_rated_employee, 'best_sale_employee': best_sale_employee,
               'month_revenue_may': month_revenue_may, 'month_revenue-march': month_revenue_march,
               'month_revenue_april': month_revenue_april}

    """
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename = "report.csv"'
    writer = csv.writer(response)
    max_rows = max(len(best_sale_employee), len(best_rated_employee), len(month_revenue_march), len(month_revenue_april), len(month_revenue_may)) #should return 5
    writer.writerow(['BR_FirstName', 'BR_LastName', 'Avg_Rating', 'BS_FirstName', 'BS_LastName', 'BS_total_sales', 'March_Sales', 'April_Sales', 'May_Sales'])

    for i in range(max_rows):
        merged=[]
        if i < len(best_rated_employee):
            merged.append(best_rated_employee[i][0])
            merged.append(best_rated_employee[i][1])
            merged.append(best_rated_employee[i][2])
        if i < len(best_sale_employee):
            merged.append(best_sale_employee[i][0])
            merged.append(best_sale_employee[i][1])
            merged.append(best_sale_employee[i][2])
        if i < len(month_revenue_march):
            merged.append(float(month_revenue_march[i][0]))
        if i < len(month_revenue_april):
            merged.append(float(month_revenue_april[i][0]))
        if i < len(month_revenue_may):
            merged.append(float(month_revenue_may[i][0]))
        merged_row = tuple(merged)
        writer.writerow(merged_row)

    return response

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    #gets called in index.js for charting data
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

        conn.close()

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




# CRUD for Order

@login_required(login_url='loginpage')
def create_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query_order')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_order.html', context)

@login_required(login_url='loginpage')
def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('query_order')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_order.html', context)


@login_required(login_url='loginpage')
def delete_order(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('query_order')
    context = {'item': order}
    return render(request, 'ecommerce_site/delete_order.html', context)


# CRUD for Supplier

@login_required(login_url='loginpage')
def create_supplier(request):
    form = SupplierForm()
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query_supplier')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_supplier.html', context)

@login_required(login_url='loginpage')
def update_supplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    form = SupplierForm(instance=supplier)
    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('query_supplier')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_supplier.html', context)


@login_required(login_url='loginpage')
def delete_supplier(request, pk):
    supplier = Supplier.objects.get(id=pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('query_supplier')
    context = {'item': supplier}
    return render(request, 'ecommerce_site/delete_supplier.html', context)

# CRUD for Product

@login_required(login_url='loginpage')
def create_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query_product')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_product.html', context)

@login_required(login_url='loginpage')
def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('query_product')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_product.html', context)


@login_required(login_url='loginpage')
def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('query_product')
    context = {'item': product}
    return render(request, 'ecommerce_site/delete_product.html', context)


# CRUD for Employee

@login_required(login_url='loginpage')
def create_employee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query_employee')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_employee.html', context)

@login_required(login_url='loginpage')
def update_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('query_employee')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_employee.html', context)


@login_required(login_url='loginpage')
def delete_employee(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == 'POST':
        employee.delete()
        return redirect('query_employee')
    context = {'item': employee}
    return render(request, 'ecommerce_site/delete_employee.html', context)


# CRUD for Customer

@login_required(login_url='loginpage')
def create_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('query_customer')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_customer.html', context)

@login_required(login_url='loginpage')
def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('query_customer')

    context = {'form': form}
    return render(request, 'ecommerce_site/create_customer.html', context)


@login_required(login_url='loginpage')
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('query_customer')
    context = {'item': customer}
    return render(request, 'ecommerce_site/delete_customer.html', context)

