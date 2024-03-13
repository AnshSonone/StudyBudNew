from django.urls import path
from .views import *

urlpatterns = [
    path("", apiPath, name='api'),
    path("rooms/", getRooms, name="getRooms"),
    path("rooms/<str:pk>/", getSingleRoom, name="getSingleRoom"),

]