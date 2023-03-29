from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from .views import SignUpView,index,about_us,contact_us,profiles_list
from .forms import loginForm

urlpatterns = [
    path('signup/',SignUpView,name="signup"),
    path('',index, name="home-page"),
    path('about-us/', about_us, name='about_us'),
    path('contact-us/', contact_us, name='contact_us'),
    path('profiles/', profiles_list, name = 'profiles-list')
]
