"""
URL configuration for BehLab project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import index
from django.conf.urls.static import static
from django.conf import settings
from .views import no_access_view, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('Users_app.urls')),  
    path('BehLabTools/', include('BehLabTools.urls')),
    path('Forum/', include('Forum.urls')),
    path('BehLabNet/', include('BehLabNet.urls')),
    path('', index, name='index'),
    path('no_access_view/', no_access_view, name='no_access_view'),
    path('about/', about, name='about')
]

#if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)