from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "category",
            "description",
            "price",
            'stock',
            "image",
            
        )
