from django.conf.urls import url
from django.urls import path
from . import views
from .views import *
urlpatterns = [
   path('', views.loginpage, name='loginpage'),
   path('/', views.loginpage, name='loginpage'),
   path('logout/', views.logoutpage, name='logout'),
   path('ad-hoc-queries/', views.querypage, name='query'),
   path('main', views.mainpage, name='mainpage'),
   path('api/chart/data', ChartData.as_view()),
   path('order/', views.query_order, name='query_order'),
   path('supplier/', views.query_supplier, name='query_supplier'),
   path('product/', views.query_product, name='query_product'),
   path('employee/', views.query_employee, name='query_employee'),
   path('customer/', views.query_customer, name='query_customer'),
   path('shipper/', views.query_shipper, name='query_shipper'),

   path('generate_report', views.generate_report, name='generate_report'),

   # CRUD paths for Order
   path('create_order/', views.create_order, name='create_order'),
   path('update_order/<str:pk>/', views.update_order, name='update_order'),
   path('delete_order/<str:pk>/', views.delete_order, name='delete_order'),

   # CRUD paths for Supplier
   path('create_supplier/', views.create_supplier, name='create_supplier'),
   path('update_supplier/<str:pk>/', views.update_supplier, name='update_supplier'),
   path('delete_supplier/<str:pk>/', views.delete_supplier, name='delete_supplier'),

   # CRUD paths for Product
   path('create_product/', views.create_product, name='create_product'),
   path('update_product/<str:pk>', views.update_product, name='update_product'),
   path('delete_product/<str:pk>', views.delete_product, name='delete_product'),

   # CRUD paths for Employee
   path('create_employee/', views.create_employee, name='create_employee'),
   path('update_employee/<str:pk>', views.update_employee, name='update_employee'),
   path('delete_employee/<str:pk>', views.delete_employee, name='delete_employee'),

   # CRUD paths for Customer
   path('create_customer/', views.create_customer, name='create_customer'),
   path('update_customer/<str:pk>', views.update_customer, name='update_customer'),
   path('delete_customer/<str:pk>', views.delete_customer, name='delete_customer'),

   # CRUD paths for Shipper
   path('create_shipper/', views.create_shipper, name='create_shipper'),
   path('update_shipper/<str:pk>', views.update_shipper, name='update_shipper'),
   path('delete_shipper/<str:pk>', views.delete_shipper, name='delete_shipper'),   #path('generate', views.generate, name='generate')
]