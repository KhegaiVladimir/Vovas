from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1, max_length=150)
    password = serializers.CharField(min_length=8)

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise ValidationError('Username already exists')


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1, max_length=150)
    password = serializers.CharField(min_length=8)


class UserConfirmSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=1, max_length=150)
    confirmation_code = serializers.CharField(min_length=6, max_length=6)

    def validate(self, data):
        username = data.get('username')
        confirmation_code = data.get('confirmation_code')

        try:
            user = User.objects.get(username=username, confirmation_code=confirmation_code, is_active=False)
            user.is_active = True
            user.save()
        except User.DoesNotExist:
            raise ValidationError('Неверный код подтверждения или пользователь уже активирован')

        return data

