from rest_framework.generics import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from apps.materials_order.models import MaterialOrder
from apps.materials_order.serializers import MaterialOrderSerializer
from users.permissions import IsMasterOrDispatcher


class MaterialOrderCreateAPIView(ListCreateAPIView):
    queryset = MaterialOrder.objects.all()
    serializer_class = MaterialOrderSerializer
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