from django.urls import path

from apps.reservations.views import ReservationCreateView

urlpatterns = [
    path('reservations/<int:pk>/', ReservationCreateView.as_view(), name='reservation-create'),
]

