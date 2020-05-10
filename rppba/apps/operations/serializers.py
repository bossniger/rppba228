from rest_framework import serializers
from apps.operations.models import OperationsList, Operation


class OperationsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperationsList
        fields = ('id', 'name', 'priority', 'product_operations',)


class OperationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = ('id', 'operation', 'product', 'element', 'element_quantity', 'time_processing',)
