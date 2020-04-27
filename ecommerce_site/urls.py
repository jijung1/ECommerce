from django.conf.urls import url
from . import views

urlpatterns = [
   url(r'^$', views.index, name='index'),
    #/ecommerce_site/101/
    url(r'^(?P<product_id>[0-9]+)/$', views.product_detail, name=''),

]