from django.contrib import admin
from django.contrib.auth import views
from django.urls import path,include
from django.views.generic import ListView,DetailView,TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',TemplateView.as_view(template_name="UserView/home.html"),name='home'),
    path('',include('accounts.urls')),
    path('jobs/',include('Jobs.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
    path('social-auth/', include('social_django.urls', namespace = 'social'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
