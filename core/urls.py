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

#   jwt imports
from rest_framework_simplejwt import views as jwt_views

# my imported views
from core.api.viewsets import NaverViewSet, ProjectViewSet, JobViewSet

# it's defining the routers to api access
router = routers.DefaultRouter()
router.register(r'navers', NaverViewSet, basename='navers')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'job_role', JobViewSet, basename='job_role')

#   paths to app access
#   here, are some paths to app developed
#   also are all routers that are defined by access api versions
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('api/v1/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
