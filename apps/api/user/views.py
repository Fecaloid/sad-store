from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response

from apps.api.user.serializers import LoginSerializer, TokenSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.data)
        if user:
            if user.is_active:
                token = Token.objects.filter(user=user).first()
                if not token:
                    token = Token.objects.create(user=user)

                token_serializer = TokenSerializer(data={'token': token.key})
                token_serializer.is_valid()
                return Response(
                    data=token_serializer.data, status=status.HTTP_200_OK
                )
            raise AuthenticationFailed('Вы забанены, идите лесом -->', status.HTTP_400_BAD_REQUEST)
        raise AuthenticationFailed('Неправильные логин или пароль', status.HTTP_400_BAD_REQUEST)
