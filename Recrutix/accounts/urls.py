from django.contrib import admin
from django.contrib.auth import views
from django.urls import path
from .views import SignUpView, delete_qualification, delete_workExperience,index,about_us,contact_us,profiles_list,subscribe,newsletter,profile_page,home, update_qualifications, update_workExperience
from .views import cv_view,resume_view,update_information,add_qualifications,add_workExperience,add_skills,blog
from .views import terms_conditions
urlpatterns = [
    path('signup/',SignUpView,name="signup"),
    path('',index, name="index"),
    path('home',home, name="home-page"),
    path("blogs/<slug:slug>",blog, name="blog"),
    path('about-us/', about_us, name='about_us'),
    path('terms-conditions/', terms_conditions, name='terms_conditions'),
    path('contact-us/', contact_us, name='contact_us'),
    path('profiles/', profiles_list, name = 'profiles-list'),
    path('subscribe/', subscribe,name = 'subscribe'),
    path('newsletter/', newsletter, name= 'newsletter'),
    path('update-information/', update_information, name="update-information"),
    path('add-qualification',add_qualifications,name="add-qualification"),
    path('update-qualification/<int:pk>',update_qualifications,name="update-qualification"),
    path('delete-qualification/<int:pk>',delete_qualification,name="delete-qualification"),
    path('add-workExperience',add_workExperience,name="add-workExperience"),
    path('update-workExperience/<int:pk>',update_workExperience,name="update-workExperience"),
    path('delete-workExperience/<int:pk>',delete_workExperience,name="delete-workExperience"),
    path('add-skills',add_skills,name='add-skills'),
    path('profile/<slug:slug>', profile_page, name='profile-page'),
    path('resume/<slug:slug>', resume_view, name='resume-view'),
    path('cv/<slug:slug>', cv_view, name='cv-view')
]
