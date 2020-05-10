from rest_framework import serializers
from apps.warehouse_materials.models import WarehouseMaterial


class WarehouseMaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseMaterial
        fields = ('id', 'element_id', 'available_quantity')
