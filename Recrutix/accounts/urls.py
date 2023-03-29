from django.contrib import admin
from django.urls import path
from .views import SignUpView,index,about_us,contact_us

urlpatterns = [
    path('signup/',SignUpView,name="signup"),
    path('',index, name="home-page"),
    path('about-us/', about_us, name='about_us'),
    path('contact-us/', contact_us, name='contact_us'),
]
