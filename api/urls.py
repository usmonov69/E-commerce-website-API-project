from django.urls import path, include 
from rest_framework import routers

from .views import home

urlpatterns = [
	path('home', home, name='home'),
	path('product/', include('api.product.urls')),
	path('order/', include('api.order.urls')),
	path('category/', include('api.category.urls')),
	path('user/',  include('api.user.urls'))
]