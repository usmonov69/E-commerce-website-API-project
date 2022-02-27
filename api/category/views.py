from django.shortcuts import render
from rest_framework import viewsets

from .models import Category
from .serializers import CategorySerializer
from api.pagination import CustomPagination

class CategoryViewSet(viewsets.ModelViewSet):
	queryset = Category.objects.all().order_by('id')
	serializer_class = CategorySerializer
	pagination_class  = CustomPagination
