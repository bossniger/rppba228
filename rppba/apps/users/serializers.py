from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'role', 'position']


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Custom serializer for registration new User-model
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Function for creating new instanse of User-model
        :param validated_data:
        :return: User-instanse
        """
        user = User(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
