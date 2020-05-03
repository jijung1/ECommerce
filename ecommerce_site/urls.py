from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
   path('', views.loginpage, name='login'),
   path('main', views.mainpage, name='main'),
   path('logout/', views.logoutpage, name='logout')
]