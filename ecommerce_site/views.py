from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
# from django.template import loader #there's a short cut using shortcuts
from .models import Product, Supplier, Customer, Order
from django.contrib.auth.decorators import login_required


def loginpage(request):
    if request.user.is_authenticated:
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
    return render(request, 'ecommerce_site/login.html')


@login_required(login_url='loginpage')
def mainpage(request):
    return render(request, 'ecommerce_site/main.html')


def logoutpage(request):
    logout(request)
    return redirect('login')






