from decimal import Decimal, InvalidOperation

from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.housing.models import Announcement


class HousingSearchByKeywordAPI(APIView):
    def get(self, request):
        keywords = request.query_params.get('q', None)  # Извлекаем параметры запроса
        if keywords:
            # Фильтруем объявления по заголовкам и описаниям с использованием Q-объектов
            hotels = Announcement.objects.filter(
                Q(title__icontains=keywords) | Q(description__icontains=keywords)
            ).values('title', 'description', 'city', 'street', 'house', 'price', 'is_active')

            if hotels.exists():
                return Response(list(hotels), status=status.HTTP_200_OK)
            else:
                return Response({"message": "No hotels found matching your search criteria."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "No keywords provided."}, status=status.HTTP_400_BAD_REQUEST)


class HousingSearchByCityAPI(APIView):
    def get(self, request):
        city = request.query_params.get('q', None)  # Извлекаем параметры запроса
        if city:
            housing = (Announcement.objects.filter(city__icontains=city).
                       values('title', 'description', 'city', 'street', 'house', 'price', 'is_active'))

            if housing.exists():
                return Response(list(housing), status=status.HTTP_200_OK)
            else:
                return Response({"message": "No hotels found matching your search criteria."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "No keywords provided."}, status=status.HTTP_400_BAD_REQUEST)



"""Поиск по цене если цена меньше указаного значения ничего не вернется"""
class HousingSearchByPriceAPI(APIView):
    def get(self, request):
        min_price = request.query_params.get('min_price', None)
        max_price = request.query_params.get('max_price', None)

        if min_price is not None and max_price is not None:
            try:
                min_price = Decimal(min_price)
                max_price = Decimal(max_price)
            except (ValueError, InvalidOperation):
                return Response({"error": "Неверный формат цены."}, status=status.HTTP_400_BAD_REQUEST)

            housing = Announcement.objects.filter(price__range=(min_price, max_price)).values(
                'title', 'description', 'city', 'street', 'house', 'price', 'is_active'
            )

            if housing.exists():
                return Response(list(housing), status=status.HTTP_200_OK)
            else:
                return Response({"message": "Не найдено объявлений, соответствующих вашему запросу."},
                                status=status.HTTP_200_OK)
        else:
            return Response({"error": "Не указаны параметры min_price и max_price."},
                            status=status.HTTP_400_BAD_REQUEST)


class HousingSearchByTypeAPI(APIView):
    def get(self, request):
        type_housing = request.query_params.get('q', None)
        if type_housing:
            types = [t.strip() for t in type_housing.split(',')]
            from django.db.models import Q
            query = Q()
            for t in types:
                query |= Q(house_type__icontains=t)

            housing = Announcement.objects.filter(query).values(
                'title', 'description', 'city', 'street', 'house', 'price', 'house_type'
            )

            if housing.exists():
                return Response(list(housing), status=status.HTTP_200_OK)
            else:
                return Response({"message": "No housing found matching your search criteria."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "No keywords provided."}, status=status.HTTP_400_BAD_REQUEST)


class HousingSearchByStreetAPI(APIView):
    def get(self, request):
        street = request.query_params.get('q', None)  # Извлекаем параметры запроса
        if street:
            housing = Announcement.objects.filter(street__icontains=street).values('title', 'description', 'city', 'street', 'house', 'price', 'is_active')

            if housing.exists():
                return Response(list(housing), status=status.HTTP_200_OK)
            else:
                return Response({"message": "No hotels found matching your search criteria."},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "No keywords provided."}, status=status.HTTP_400_BAD_REQUEST)

class HousingSearchByCountRoomAPI(APIView):
    def get(self, request):
        min_room = request.query_params.get('min_room', None)
        max_room = request.query_params.get('max_room', None)

        if min_room is not None and max_room is not None:
            try:
                min_price = int(min_room)
                max_price = int(max_room)
            except (ValueError, InvalidOperation):
                return Response({"error": "Неверный формат."}, status=status.HTTP_400_BAD_REQUEST)

            housing = Announcement.objects.filter(count_room__range=(min_price, max_price)).values(
                'title', 'description', 'city', 'street', 'house', 'price', 'is_active', 'count_room'
            )

            if housing.exists():
                return Response(list(housing), status=status.HTTP_200_OK)
            else:
                return Response({"message": "Не найдено объявлений, соответствующих вашему запросу."},
                                status=status.HTTP_200_OK)
        else:
            return Response({"error": "Не указаны параметры min_room и max_room."},
                            status=status.HTTP_400_BAD_REQUEST)
