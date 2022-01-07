from rest_framework.serializers import ModelSerializer

from .models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = ["session_id", "timestamp", "category", "name", "data"]
