from django.db import models

# Create your models here.
from django.db import models
from api.user.models import CustomUser


class Order(models.Model):
	user = models.ForeignKey(CustomUser, related_name='orders', on_delete=models.CASCADE)
	product_names = models.CharField(max_length=150)
	total_amount = models.IntegerField(default=0)
	total_products = models.CharField(max_length=250, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	paid_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
	stripe_token = models.CharField(max_length=100)
	transaction_id = models.CharField(max_length=20,default=0)

	def __str__(self):
		return f"{self.product_name}"
