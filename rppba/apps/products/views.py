from rest_framework import generics
from rest_framework import permissions
from .serializers import ProductSerializers
from .models import Product
from users.permissions import IsTechnologist


class ProductListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_action_classes = {
        'POST': [
            permissions.IsAuthenticated(),
            IsTechnologist(),
        ],
        'GET': [
            permissions.IsAuthenticated(),
        ],
    }

    def get_permissions(self):
        return self.permission_action_classes[self.request.method]


class ProductUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializers
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [
                permissions.IsAuthenticated(),
            ]
        else:
            return [
                permissions.IsAuthenticated(),
                IsTechnologist(),
            ]
