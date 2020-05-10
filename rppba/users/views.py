from .serializers import UserRegisterSerializer
from rest_framework import generics


class Register(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = []
