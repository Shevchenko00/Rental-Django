from django.db import models
from django.db.models import ForeignKey

from apps.housing.models import Announcement
from apps.users.models import User


class Reservation(models.Model):
    user = ForeignKey(User, related_name='reservations', on_delete=models.CASCADE)
    announcement = ForeignKey(Announcement, related_name='reservations', on_delete=models.CASCADE, null=True)
    start_date = models.DateField(verbose_name='Start date', null=False, blank=False)
    end_date = models.DateField(verbose_name='End date', null=False, blank=False)
    comment = models.TextField(verbose_name='Comment', null=True, blank=True)
    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        unique_together = (('user', 'start_date', 'end_date'),)
