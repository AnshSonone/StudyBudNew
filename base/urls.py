from django.urls import path
from .views import *

urlpatterns = [
    # Authentication routes
    path('login/', loginPage, name='login'),
    path('logout/', logoutPage, name='logout'),
    path('register/', registerPage, name='register'),

    # Home page routes
    path('', Home, name='home'),
    path('room/<str:pk>/', room, name='room'),
    path('profile/<str:pk>/', userProfile, name='userProfile'),

    # CRUD routes
    path('create-room', createRoom, name='createRoom'),
    path('update-room/<str:pk>/', updateRoom, name='updateRoom'),
    path('delete-room/<str:pk>/', deleteRoom, name='deleteRoom'),
    path('delete-message/<str:pk>/', deleteMessage, name='deleteMessage'),

    path('update-user/', updateUser, name='updateUser'),
    path('topics/', topicPage, name='topics'),
    path('activity/', activityPage, name='activity'),
]