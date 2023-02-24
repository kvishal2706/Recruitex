from django.contrib import admin
from django.urls import path
from .views import SignUpView,index

urlpatterns = [
    path('signup/',SignUpView,name="signup"),
    path('',index, name="home-page")
]
