from django.shortcuts import render
from .serializers import UserCreateSerializer, UserAuthSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def registration_api_view(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user= User.objects.create_user(username=username, password=password, is_active=False)
        return Response(data={})


@api_view(['POST'])
def authorization_api_view(request):
    if request.method == 'POST':
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)

        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response(data={'token': token.key})
        return Response(data={'error':'User credentials are wrong'})