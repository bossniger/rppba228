from rest_framework import generics
from rest_framework import permissions
from .serializers import OperationsListSerializer, OperationSerializer
from .models import OperationsList, Operation


class ProductOperationListCreateListApiView(generics.ListCreateAPIView):

    serializer_class = OperationSerializer
    queryset = Operation.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]


class ProductOperationUpdateApiView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = OperationSerializer
    queryset = Operation.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]


class OperationListCreateListApiView(generics.ListCreateAPIView):

    serializer_class = OperationsListSerializer
    queryset = OperationsList.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]


class OperationListUpdateApiView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = OperationsListSerializer
    queryset = OperationsList.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]

