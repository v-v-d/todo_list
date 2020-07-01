from djoser.serializers import UserCreateSerializer

from authapp.models import TodoUser


class TodoUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = TodoUser
        fileds = ('id', 'username', 'email', 'password')
