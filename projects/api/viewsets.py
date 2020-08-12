#   framework imports
from rest_framework.viewsets import ModelViewSet

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
    