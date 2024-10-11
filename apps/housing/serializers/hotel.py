from rest_framework import serializers
from apps.housing.models.announcement import Announcement


class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'description', 'city', 'street', 'house', 'price', 'is_active', 'house_type', 'count_room', 'landlord']
        read_only_fields = ['landlord']
