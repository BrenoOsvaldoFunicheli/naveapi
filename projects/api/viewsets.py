#   framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend

# jwt import
from rest_framework.permissions import IsAuthenticated

#   important class
from projects.models import Project
from .serializers import ProjectSerializer, DetailProjectSerializer


class ProjectViewSet(ModelViewSet):
    """
        Class to handle the serializer and data
    """
    # permission_classes = (IsAuthenticated, )
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', )

    def get_queryset(self):
        return Project.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailProjectSerializer
        else:
            return ProjectSerializer

    


