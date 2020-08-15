#   my models that project uses
from core.models import Naver, Project, Technologie, JobRole

#   rest framework's dependecies
from rest_framework.serializers import ModelSerializer

class ProjectSerializer(ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'name']


class JobSerializer(ModelSerializer):
    class Meta:
        model = JobRole
        fields = ['id', 'name', 'description']


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
            'id', 'name', 'birthdate',  'admission_date', 'end_date', 'job', 'projects'
        )


class DetailProjectSerializer(ModelSerializer):
    naver_set = NaverSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'naver_set']
