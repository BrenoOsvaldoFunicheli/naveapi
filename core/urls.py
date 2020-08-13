"""naveapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
# needed imports to django rest framework
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# my imported views
from core.api.viewsets import NaverViewSet

# it's defining the routers to api access
router = routers.DefaultRouter()
router.register(r'navers', NaverViewSet, basename='navers')

#   paths to app access
#   here, are some paths to app developed
#   also are all routers that are defined by access api versions
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
