from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from apps.warehouse_materials.models import WarehouseMaterial
from apps.warehouse_materials.serializers import WarehouseMaterialSerializer


class WarehouseMaterialsListAPIView(ListCreateAPIView):
    queryset = WarehouseMaterial.objects.all()
    serializer_class = WarehouseMaterialSerializer
    permission_classes = [
        permissions.AllowAny,
    ]


class WarehouseMaterialsRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = WarehouseMaterial.objects.all()
    serializer_class = WarehouseMaterialSerializer
    permission_classes = [
        permissions.AllowAny,
    ]
