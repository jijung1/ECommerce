from django.conf.urls import url
from django.urls import path
from . import views
from .views import *
urlpatterns = [
   path('', views.loginpage, name='loginpage'),
   path('/', views.loginpage, name='loginpage'),
   path('logout/', views.logoutpage, name='logout'),
   path('main/', views.mainpage, name='main'),
   path('ad-hoc-queries/', views.querypage, name='query'),
   path('api/chart/data', ChartData.as_view())
]