from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters

from rest_framework.generics import RetrieveUpdateDestroyAPIView

from apps.housing.models import Announcement
from apps.housing.serializers.change_active import ChangeActiveSerializer
from apps.housing.serializers.hotel import AnnouncementSerializer
from apps.housing.views.search_views import AnnouncementFilter


class HousingCreateAPI(generics.CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class HousingDetailAPI(generics.RetrieveAPIView):
    queryset = Announcement.objects.all()  # Получаем все объекты
    serializer_class = AnnouncementSerializer
    lookup_field = 'pk'


class HousingUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer


class HouseChangeActiveAPI(generics.UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = ChangeActiveSerializer
    lookup_field = 'pk'


class HousingSearch(generics.ListAPIView):
    queryset = Announcement.objects.filter(is_active="Активно")  # Только активные квартиры
    serializer_class = AnnouncementSerializer  # Сериализатор для объектов
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = AnnouncementFilter  # Указываем фильтр
