from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.number_choices.country_code import COUNTRY_CODES


class User(AbstractUser):
    first_name = models.CharField(max_length=10, null=False, verbose_name='Имя')
    last_name = models.CharField(max_length=30, null=False, verbose_name='Фамилия')
    date_birth = models.DateField(null=False, verbose_name='Дата рождения',
                                  help_text='Дата рождения в формате ГОД-МЕСЯЦ-ДАТА')
    email = models.EmailField(unique=True, verbose_name='Email')
    country = models.CharField(max_length=30, null=False, verbose_name='Страна')
    city = models.CharField(max_length=30, null=False, verbose_name='Город')
    country_code = models.CharField(max_length=30, null=False, choices=COUNTRY_CODES, verbose_name='Код вашей страны')
    phone = models.CharField(max_length=30, blank=True, help_text='Введите номер телефона без учета кода',
                             verbose_name='Номер телефона')


    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='Группы, к которым принадлежит этот пользователь. '
                  'Пользователь получит все разрешения, предоставленные каждой из своих групп.',
        verbose_name='Группы',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',  # Уникальное имя для обратного доступа
        blank=True,
        help_text='Конкретные разрешения для этого пользователя.',
        verbose_name='Разрешения пользователя',
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
