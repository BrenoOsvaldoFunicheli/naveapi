
# needed imports to django rest framework
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

# my imported views
from projects.api.viewsets import ProjectViewSet

# it's defining the routers to api access
router = routers.DefaultRouter()

router.register(r'projects', ProjectViewSet, basename='project')

#   paths to app access
#   here, are some paths to app developed
#   also are all routers that are defined by access api versions
urlpatterns = [
    path('api/v1/', include(router.urls)),
]
