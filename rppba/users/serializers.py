from rest_framework import serializers

from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    Custom serializer for registration new User-model
    """
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'name', 'role', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Function for creating new instanse of User-model
        :param validated_data:
        :return: User-instanse
        """
        user = User(
            username=validated_data['username'],
            name=validated_data['name'],
            role=validated_data['role'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user