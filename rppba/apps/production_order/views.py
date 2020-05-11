from rest_framework import generics
from rest_framework import permissions

from users.permissions import IsDispatcher, IsMasterOrDispatcher
from .serializers import ProductionOrderSerializer
from .models import ProductionOrder


class ProductionOrderListCreateAPIView(generics.ListCreateAPIView):

    serializer_class = ProductionOrderSerializer
    queryset = ProductionOrder.objects.all()
    permission_action_classes = {
        'POST': [
            permissions.IsAuthenticated(),
            IsMasterOrDispatcher(),
        ],
        'GET': [
            permissions.IsAuthenticated(),
        ],
    }

    def get_permissions(self):
        return self.permission_action_classes[self.request.method]


class ProductionOrderUpdateAPIView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductionOrderSerializer
    queryset = ProductionOrder.objects.all()
    permission_action_classes = {
        'PATCH': [
            permissions.IsAuthenticated(),
            IsMasterOrDispatcher(),
        ],
        'GET': [
            permissions.IsAuthenticated(),
        ],
        'PUT': [
            permissions.IsAuthenticated(),
            IsMasterOrDispatcher(),
        ],
    }

    def get_permissions(self):
        return self.permission_action_classes[self.request.method]
