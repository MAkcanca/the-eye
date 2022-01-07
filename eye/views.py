from django.http import HttpResponse
from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import Event
from .serializers import EventSerializer
from .tasks import log_event


def index(request):
    return HttpResponse("Hello from The Eye!")


class EventView(ListCreateAPIView):
    serializer_class = EventSerializer
    queryset = Event.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            log_event.delay(data)
            return Response({"success": True}, status=status.HTTP_201_CREATED)
        else:
            print("ERRORS", serializer.errors)
            return Response({"success": False}, status=status.HTTP_201_CREATED)
