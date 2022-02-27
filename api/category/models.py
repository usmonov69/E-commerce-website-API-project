from django.db import models



class Category(models.Model):
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	
	class Meta:
		verbose_name_plural="Categories"

	def __str__(self):
		return f"{self.name}"