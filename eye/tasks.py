from celery import shared_task

from .serializers import EventSerializer


@shared_task
def log_event(data):
    serializer = EventSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
