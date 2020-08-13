#   framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

#   important class
from projects.models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(ModelViewSet):
    """
        Class to handle the serializer and data
    """
    # queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()
    
    # @action(methods=['get'], detail=True)
    # def search_projects(self, request, pk=None):
    #     pass