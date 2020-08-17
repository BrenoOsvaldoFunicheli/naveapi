# django imports
from django.contrib import admin
from django.urls import path, include

# needed imports to django rest framework
from rest_framework import routers

#   jwt imports
from rest_framework_simplejwt import views as jwt_views

# my imported views
from core.api.viewsets import *
from users.api.viewsets import UserSerializer

from rest_framework_jwt.views import obtain_jwt_token

# it's defining the routers to api access
router = routers.DefaultRouter()
router.register(r'navers', NaverViewSet, basename='navers')
router.register(r'projects', ProjectViewSet, basename='project')
router.register(r'job_role', JobViewSet, basename='job_role')
router.register(r'technologies', TechnologiesViewSet, basename='tecnologie')


#   paths to app access
#   here, are some paths to app developed
#   also are all routers that are defined by access api versions
urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/v1/login/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
#     path('api/v1/login/',obtain_jwt_token, name='token_obtain_pair'),
    path('api/v1/login/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),
]
