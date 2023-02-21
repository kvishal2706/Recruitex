# config/urls.py
from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from .views import JobsListView,JobsUpdateView,JobsDeleteView,JobsDetailView,JobsCreateView

urlpatterns = [
    path('', JobsListView.as_view(),name='jobs_list'), # new
    path('<int:pk>/', JobsDetailView.as_view(),name='jobs_detail'), # new
    path('<int:pk>/edit', JobsUpdateView.as_view(),name='jobs_edit'), # new
    path('<int:pk>/delete', JobsDeleteView.as_view(),name='jobs_delete'), # new
    path('new/', JobsCreateView.as_view(),name='jobs_new'), # new
]