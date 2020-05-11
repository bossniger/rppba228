from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from apps.orders.models import Order
from apps.orders.serializers import OrderSerializer
from users.permissions import IsDispatcher


class OrdersListAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_action_classes = {
        'POST': [
            permissions.IsAuthenticated(),
            IsDispatcher(),
        ],
        'GET': [
            permissions.IsAuthenticated(),
        ],
    }

    def get_permissions(self):
        return self.permission_action_classes[self.request.method]


class OrdersRetrieveAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_action_classes = {
        'PATCH': [
            permissions.IsAuthenticated(),
            IsDispatcher(),
        ],
        'GET': [
            permissions.IsAuthenticated(),
        ],
        'PUT': [
            permissions.IsAuthenticated(),
            IsDispatcher(),
        ],
    }