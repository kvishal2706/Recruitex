from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.room, name='room'),
    path('checkroom/<slug:slug>', views.check_room, name='checkroom'),
    path('send', views.send, name='send'),
    path('getMessages/<str:room>/', views.getMessages, name='getMessages'),
]