from random import randint, random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserCreateSerializer, UserAuthSerializer, UserConfirmSerializer
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

def generate_confirmation_code():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

@api_view(['POST'])
def registration_api_view(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')
        confirmation_code = ''.join([str(randint(0, 9)) for _ in range(6)])  # Генерация кода подтверждения

        user = User.objects.create_user(username=username, password=password, confirmation_code=confirmation_code,
                                        is_active=False)
        return Response(data={"user_id": user.id, "confirmation_code": confirmation_code},
                        status=status.HTTP_201_CREATED)








@api_view(['POST'])
def authorization_api_view(request):
    if request.method == 'POST':
        serializer = UserAuthSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data.get('username')
        password = serializer.validated_data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, create = Token.objects.get_or_create(user=user)
            return Response(data={"key": token.key})
        return Response(status=status.HTTP_401_UNAUTHORIZED, data = {'error':"User credentions are wrong"})


@api_view(['POST'])
def user_confirm_api_view(request):
    if request.method == 'POST':
        serializer = UserConfirmSerializer(data=request.data)
        if serializer.is_valid():
            return Response({"message": "Пользователь успешно подтвержден"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
