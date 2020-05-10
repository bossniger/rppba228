from rest_framework import generics
from rest_framework import permissions
from .serializers import ProductSerializers
from .models import Product


class ProductListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]


class ProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
