import django_filters
from django_filters import *

from .models import *


class ProductFilter(django_filters.FilterSet):
    price__gt = django_filters.NumberFilter(field_name='price', lookup_expr='gt')
    price__lt = django_filters.NumberFilter(field_name='price', lookup_expr='lt')
    units_in_stock__gt = django_filters.NumberFilter(field_name='units_in_stock', lookup_expr='gt')
    units_in_stock__lt = django_filters.NumberFilter(field_name='units_in_stock', lookup_expr='lt')
    units_on_order__gt = django_filters.NumberFilter(field_name='units_on_order', lookup_expr='gt')
    units_on_order__lt = django_filters.NumberFilter(field_name='units_on_order', lookup_expr='lt')

    class Meta:
        model = Product
        fields = []


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_ordered', lookup_expr='gte')
    end_date = DateFilter(field_name='date_ordered', lookup_expr='lte')
    class Meta:
        model = Order
        fields = ['tracking_number', 'status', 'date_ordered']
       # exclude = [ ]

