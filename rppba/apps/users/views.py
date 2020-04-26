from .serializers import UserRegisterSerializer, UserSerializer
from rest_framework import generics, permissions
from .permissions import IsNotAuthenticated


class UserRegister(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [IsNotAuthenticated, ]


class UserDetailUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
