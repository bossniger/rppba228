from rest_framework import generics
from rest_framework import permissions
from .serializers import ProductionOrderSerializer
from .models import ProductionOrder


class ProductionOrderListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = ProductionOrderSerializer
    queryset = ProductionOrder.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]


class ProductionOrderUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductionOrderSerializer
    queryset = ProductionOrder.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
