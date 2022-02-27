from django.contrib.auth.models import User
from django.http import JsonResponse





def home(request):
    return JsonResponse({
    	'info':"Django  Ecommerce Project API ",
    	'developer':"Rakhmat Usmonov"})