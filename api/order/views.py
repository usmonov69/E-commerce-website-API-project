from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets

from .models import Order 
from .serializers import OrderSerializer
from api.pagination import CustomPagination
# User Authentication view
def validate_user(id,token):
	"""Allow ordering for only authenticated users"""
	UserModel = get_user_model()

	try:
		user = UserModel.objects.get(pk=id)
		# Check if Session Token matches User Token
		if user.session_token == token:
			return True # User is authenticated
		else:
			return False # User is unauthenticated 
	except UserModel.DoesNotExist:
		return False

# Add Order view
def add_order(request, id, token):
	if not validate_user(id, token):
		return JsonResponse({'error':"Please login again", 'code':'1'})

	if request.method == 'POST':
		user_id = id
		transaction_id = request.POST['transaction_id']
		amount = request.POST['amount']
		products = request.POST['products']
		total_no_products = len(products.split(','[:-1]))

		UserModel = get_user_model()

		try:
			user = UserModel.objects.get(pk=user_id)
		except UserModel.DoesNotExist:
			return JsonResponse({'error':'User does not exist'})

		order_detail = Order(user=user,product_names=products,
				total_no_products=total_no_products,
				transaction_id=transaction_id,
				total_amount=amount,)
		order_detail.save()

		return JsonResponse({'success':True, 'error':False, 'msg':'Order placed siccessfully'})

#Order View
class OrderViewSet(viewsets.ModelViewSet):
	queryset = Order.objects.all().order_by('id')
	serializer_class = OrderSerializer
	pagination_class  = CustomPagination