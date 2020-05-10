from rest_framework import serializers
from apps.products.models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'model_name', 'type', 'product_time_production')
