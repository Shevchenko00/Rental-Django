from django.contrib.auth.backends import ModelBackend
from apps.users.models import User  # Убедитесь, что путь к вашей модели User правильный


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=username)  # Используем email для поиска пользователя
        except User.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None
