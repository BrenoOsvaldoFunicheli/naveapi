#   my models that project uses
from core.models import Naver, Project, Technologie

#   rest framework's dependecies
from rest_framework.serializers import ModelSerializer


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
        fields = ['id', 'name', 'navers']


class NaverSerializer(ModelSerializer):

    """
        Serializer that will be provid serialization
    """
    class Meta:
        model = Naver
        fields = ('id', 'name', 'birthdate', 'admission_date', 'job')


class DetailNaverSerializer(ModelSerializer):
    """
        Serializer that will be provid serialization
    """
    projects = ProjectSerializer(
        many=True)  # can be used to show nested relation project

    class Meta:
        model = Naver
        fields = (
            'id', 'name', 'birthdate',  'admission_date',  'job', 'projects'
        )
