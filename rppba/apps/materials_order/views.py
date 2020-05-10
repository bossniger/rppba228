from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from apps.materials_order.models import MaterialOrder
from apps.materials_order.serializers import MaterialOrderSerializer


class MaterialOrderCreateAPIView(ListCreateAPIView):
    queryset = MaterialOrder.objects.all()
    serializer_class = MaterialOrderSerializer
    permission_classes = [
        permissions.AllowAny,
    ]