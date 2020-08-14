#   restframework's imports
from rest_framework.serializers import ModelSerializer

#   my models that project uses
from core.models import Naver, Project

#   my serializers to implement Nested Relations
from projects.api.serializers import ProjectSerializer


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
