from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    """Custom serializer for user creation."""

    class Meta(BaseUserCreateSerializer.Meta):
        # model = BaseUserCreateSerializer.Meta.model

        fields = ('id', 'username', 'email',
                  'password', 'first_name', 'last_name')


class UserSerializer(BaseUserSerializer):
    """Custom serializer for user representation."""

    class Meta(BaseUserSerializer.Meta):
        # model = BaseUserSerializer.Meta.model

        fields = ('id', 'username', 'email',
                  'first_name', 'last_name')
