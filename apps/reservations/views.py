from django.shortcuts import render
from django.views.generic import ListView
from rest_framework import generics, permissions
from rest_framework.exceptions import NotFound

from apps.housing.models import Announcement
from apps.reservations.models.reservations import Reservation
from apps.reservations.serializers.reservation_serializer import ReservationSerializer


# Create your views here.
class ReservationCreateView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def perform_create(self, serializer):
        announcement_id = self.kwargs.get('pk')
        try:
            announcement = Announcement.objects.get(pk=announcement_id)
        except Announcement.DoesNotExist:
            raise NotFound('Announcement not found.')

        serializer.save(user=self.request.user, announcement=announcement)
