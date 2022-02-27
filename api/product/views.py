from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer   
from api.pagination import CustomPagination


class ProductList(ModelViewSet):
	queryset = Product.objects.all().order_by('id')
	pagination_class = CustomPagination
	serializer_class = ProductSerializer
