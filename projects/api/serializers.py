#   rest framework's dependecies
from rest_framework.serializers import ModelSerializer

#   my models to use with restframework
from projects.models import Project, Technologie

#   external serializer, that need to setting nested fields
# from core.api.serializers import NaverSerializer


class ProjectSerializer(ModelSerializer):
    

    
    class Meta:
        model = Project
        fields = ['id', 'name']


class DetailProjectSerializer(ModelSerializer):

    # navers = NaverSerializer

    class Meta:
        model = Project
        fields = ['id', 'name','navers']
