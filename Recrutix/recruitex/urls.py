from django.contrib import admin
from django.urls import path,include
from django.views.generic import ListView,DetailView,TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',TemplateView.as_view(template_name="UserView/home.html"),name='home'),
    path('',include('accounts.urls')),
    path('jobs/',include('Jobs.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
]
