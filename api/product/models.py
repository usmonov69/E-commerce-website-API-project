from django.db import models
from django.template.defaultfilters import slugify
from api.category.models import Category 

class Product(models.Model):
	category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
	name = models.CharField(max_length=220)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)
	stock = models.CharField(max_length=50)
	slug = models.SlugField( blank=True)
	image = models.ImageField(upload_to='uploads/', blank=True, null=True)
	is_active = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('-created_at',)

	def __str__(self):
		return str(self.name)


	def save(self, *args, **kwargs):#for url-slug
		if self.slug == "":
			self.slug = slugify(self.name)
		return super().save(*args, **kwargs)





	def get_image(self):
		if self.image:#for frontend
			return 'http://127.0.0.1:8000' + self.image.url
		return ''
    
