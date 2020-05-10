from rest_framework import serializers
from apps.production_order.models import ProductionOrder


class ProductionOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionOrder
        fields = ('id', 'product', 'product_quantity', 'lead_time_production', 'production_start',
                  'status', 'master')
