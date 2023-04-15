from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView 
from .views import JobsListView,JobsDetailView,JobsCreateView,UpdateJob, DeleteJob,job_applicants

urlpatterns = [
    path('', JobsListView,name='jobs_list'), 
    path('<slug:slug>', JobsDetailView,name='job_details'), 
    path('edit_job/<slug:slug>', UpdateJob,name='job_edit'), 
    path('delete_job/<slug:slug>', DeleteJob,name='job_delete'), 
    path('new/', JobsCreateView,name='jobs_new'), 
    path('applicants/<slug:slug>',job_applicants,name='job-applicants')
]
