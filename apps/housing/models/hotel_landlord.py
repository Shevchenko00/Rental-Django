from django.db import models
from django.contrib.auth.models import AbstractUser
from apps.number_choices.country_code import COUNTRY_CODES


class Landlord(AbstractUser):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=30, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country_code = models.CharField(max_length=30, choices=COUNTRY_CODES, blank=True, verbose_name='Код вашей страны')
    phone = models.CharField(max_length=30, blank=True, help_text='Введите номер телефона без учета кода',
                             verbose_name='Номер телефона')

    def __str__(self):
        return self.first_name, self.last_name
