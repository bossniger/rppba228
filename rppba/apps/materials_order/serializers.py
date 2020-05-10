from rest_framework import serializers
from apps.materials_order.models import MaterialOrder


class MaterialOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaterialOrder
        fields = ('id', 'user_id', 'warehouse_material', 'quantity')
