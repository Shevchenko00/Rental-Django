from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.housing.models import Announcement
from apps.housing.serializers.change_active import ChangeActiveSerializer
from apps.housing.serializers.hotel import AnnouncementSerializer
from apps.housing.views.search_views import AnnouncementFilter
from apps.users.permissions.landlord_permissions import IsLandlordOwner


class HousingCreateAPI(generics.CreateAPIView):
    permission_classes = [AllowAny]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class HousingDetailAPI(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    lookup_field = 'pk'


class HousingUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsLandlordOwner]
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer



class HouseChangeActiveAPI(generics.UpdateAPIView):
    permission_classes = [IsLandlordOwner]
    queryset = Announcement.objects.all()
    serializer_class = ChangeActiveSerializer
    lookup_field = 'pk'


class HousingSearch(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = Announcement.objects.filter(is_active="Активно")
    serializer_class = AnnouncementSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = AnnouncementFilter

