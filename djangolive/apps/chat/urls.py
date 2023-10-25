# urls.py
from django.urls import path
from djangolive.apps.chat import views

urlpatterns = [
    path('chat/<str:room_name>/', views.chat, name='chat'),
]
