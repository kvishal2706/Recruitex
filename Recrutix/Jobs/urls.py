from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from .views import JobsListView,JobsDetailView,JobsCreateView,UpdateJob, DeleteJob

urlpatterns = [
    path('', JobsListView,name='jobs_list'), # new
    path('<slug:slug>', JobsDetailView,name='job_details'), # new
    path('edit_job/<slug:slug>', UpdateJob,name='job_edit'), # new
    path('delete_job/<slug:slug>', DeleteJob,name='job_delete'), # new
    path('new/', JobsCreateView.as_view(),name='jobs_new'), # new
]
