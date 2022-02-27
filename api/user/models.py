from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import get_random_code

GENDER_CHOICES = (
	('Male','Male'),
	('Female','Female'),
	)


class CustomUser(AbstractUser):
	name = models.CharField(max_length=50, default="Anonymous")
	email = models.EmailField(max_length=220, unique=True)
	username = models.CharField(max_length=50, unique=True)
	phone = models.CharField(max_length=20, blank=True, null=True)
	gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True, null=True)
	session_token = models.CharField(max_length=10, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


	def save(self, *args, **kwargs):
		if self.session_token == '0':
			self.session_token = get_random_code()
		return super().save(*args, **kwargs)
