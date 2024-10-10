from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken

from apps.users.serializers.login_serializer import LoginSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Получаем пользователя из сериализатора
        user = serializer.validated_data['user']

        # Генерируем токен
        token = AccessToken.for_user(user)

        return Response({
            "access": str(token),
            "user": {
                "email": user.email,
                "id": user.id,
            },
        })