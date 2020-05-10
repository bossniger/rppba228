from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from users.permissions import IsTechnologist
from apps.elements.models import Element
from apps.elements.serializers import ElementsSerializer


class ElementListCreateAPIView(ListCreateAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = (
        permissions.IsAuthenticated,
        IsTechnologist(),
    )
    

class ElementUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Element.objects.all()
    serializer_class = ElementsSerializer
    permission_classes = [
        # permissions.IsAuthenticated,
        # IsTechnologist,
    ]
