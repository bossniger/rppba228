from rest_framework import generics
from rest_framework import permissions
from .serializers import OperationsListSerializer, OperationSerializer
from .models import OperationsList, Operation
from ..elements.permissions import IsTechnologist


class ProductOperationListCreateListApiView(generics.ListCreateAPIView):

    serializer_class = OperationSerializer
    queryset = Operation.objects.all()
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


class ProductOperationUpdateApiView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = OperationSerializer
    queryset = Operation.objects.all()

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


class OperationListCreateListApiView(generics.ListCreateAPIView):

    serializer_class = OperationsListSerializer
    queryset = OperationsList.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsTechnologist,
    ]


class OperationListUpdateApiView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = OperationsListSerializer
    queryset = OperationsList.objects.all()
    permission_classes = [
        permissions.IsAuthenticated,
        IsTechnologist,
    ]

