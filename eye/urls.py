from django.urls import path

from .views import EventView, index

urlpatterns = [
    path("", index),
    path("event/", EventView.as_view()),
]
