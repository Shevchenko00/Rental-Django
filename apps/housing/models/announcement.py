from django.db import models
from django.db.models import CharField


class Announcement(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name='Заголовок',
                             help_text='(поле является обязательным)')
    description = models.TextField(null=False, blank=False, verbose_name='Описание',
                                   help_text='(поле является обязательным)')
    house_type = models.CharField(max_length=10, null=False, blank=False, verbose_name='Тип жилья', default=None)
    count_room = models.SmallIntegerField(null=False, verbose_name='Количество комнат', default=None)
    city = models.CharField(max_length=100, null=False, verbose_name='Город', help_text='(поле является обязательным)')
    street = models.CharField(max_length=100, null=False, verbose_name='Улица',
                              help_text='(поле является обязательным)')
    house = models.CharField(max_length=10, null=False, verbose_name='Дом', help_text='(поле является обязательным)')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена', null=False, blank=True,
                                default=0.00)
    ACTIV_CHOICE = [
        ('Активно', 'Активно'),
        ('Неактивно', 'Неактивно')
    ]
    is_active = models.CharField(max_length=10, choices=ACTIV_CHOICE, default='Неактивно',
                                help_text='(поле является обязательным)', verbose_name='Статус объявления')
    # tenant =
    class Meta:
        indexes = [
            models.Index(fields=['city', 'street', 'house']),
        ]
        verbose_name = 'Housing'
        verbose_name_plural = 'Housings'

    def __str__(self):
       return f'{self.title}, {self.description}'