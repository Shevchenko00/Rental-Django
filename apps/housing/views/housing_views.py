from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

from apps.housing.models import Announcement
from apps.housing.serializers.hotel import AnnouncementSerializer


class HousingGetAPI(APIView):
    def get(self, request, pk=None):
        if pk:
            try:
                apartment = Announcement.objects.get(pk=pk)  # Модель Announcement, а не сериализатор
                serializer = AnnouncementSerializer(apartment)
                return Response(serializer.data)
            except Announcement.DoesNotExist:
                return Response({"error": "Apartment not found"}, status=404)
        else:
            # Используем модель для фильтрации, а сериализатор для преобразования данных
            apartments = Announcement.objects.filter(is_active="Активно").values(
                'title', 'description', 'street', 'house', 'count_room', 'price', 'house_type'
            )
            return JsonResponse(list(apartments), safe=False)
class HousingCreateAPI(APIView):
    def post(self, request):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'message': f"House for rent: '{serializer.validated_data['title']}' successfully created.",
                'housing': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """Обновляет данные об отеле"""
        house = self.get_hotel(pk)
        serializer = AnnouncementSerializer(house, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """Удаляет отель"""
        house = self.get_hotel(pk)
        house.delete()
        return Response({'message': 'House for rent deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)


class HouseChangeActiveAPI(APIView):
    def put(self, request, pk):
        """Меняет статус активности отеля"""
        house = get_object_or_404(Announcement, pk=pk)
        data = request.data.copy()

        # Устанавливаем статус активности на основе запроса
        if 'activate' in data and data['activate'] == True:
            data['is_active'] = 'Активно'
        else:
            data['is_active'] = 'Неактивно'

        serializer = AnnouncementSerializer(house, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

