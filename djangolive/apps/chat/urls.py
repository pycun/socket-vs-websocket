# urls.py
from django.urls import path
from djangolive.apps.chat import views
from djangolive.apps.chat.views_socket.sse_events import stream, index

urlpatterns = [
    path('chat/<str:room_name>/', views.chat, name='chat'),
    path('login/', views.login, name='login'),
    path('stream/', stream, name='sse'),
    path('', index, name='index'),
]
