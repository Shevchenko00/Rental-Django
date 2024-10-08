from rest_framework.serializers import ModelSerializer

from apps.housing.models import Announcement


class SearchKeywordSerializer(ModelSerializer):
    class Meta:
        models = Announcement
        fields = ['title', 'description']
