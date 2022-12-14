"""faceRecog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from faceRecog import views as app_views
from django.urls import path, include
from django.views.generic.base import TemplateView 

urlpatterns = [
    path('', app_views.index),
    url(r'^error_image$', app_views.errorImg),
    url(r'^create_dataset$', app_views.create_dataset),
    path('detect/', app_views.detect),
    url(r'^admin/', admin.site.urls),
    #url(r'^records/', include('records.urls')),
    path('<str:id>', app_views.displayImage),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('accounts/', include('accounts.urls')), 
    path('deny/<str:id>', app_views.delete),
    path('attendance/<str:id>', app_views.attendance),
    path('mark/<str:id>', app_views.mark)
]
