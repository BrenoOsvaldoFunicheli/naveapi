# framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from django_filters.rest_framework import DjangoFilterBackend

# django shortcut
from django.shortcuts import get_object_or_404

# my imported models
from core.models import Naver, Project, JobRole
from core.api.query_string import NaversFilters
from core.api.serializers import *

# jwt import
from rest_framework.permissions import IsAuthenticated


class NaverViewSet(ModelViewSet):
    """
        Viewset that represents the naver access
    """

    # serializer_class = NaverSerializer

    def get_queryset(self):
        """
            Parameters
            ----------
            None
                This function doesn't has some parameters,
                because all params are providing by request session.

            Returns
            -------
            QuerySet

                This function returns query with objects
                that can be filtered or not, if the.
        """
        params = self.request.query_params
        n_filter = NaversFilters(params)
        return n_filter.get_objects()

    # def retrieve(self, request,pk=None):
    #     queryset = Naver.objects.all()
    #     naver = get_object_or_404(queryset, pk=pk)
    #     serializer = NaverSerializer(naver)
    #     return Response(serializer.data)

    def get_serializer_class(self):
        """

            Returns
            -------
            Serializer

                This function returns Serializer class
                that going to process the request
        """
        if self.action == 'retrieve':
            return DetailNaverSerializer
        else:
            return NaverSerializer

    def create(self, validated_data):
        """
            Parameters
            ----------

                Send only JSON objects else the django will be get
                the Immutable QueryDict, and you won't use the pop
                method and you'll return the error to API. 
        """

        #   first we get the job reference that was send in Body
        job_id = validated_data.data.pop('job_role', None)
        job = JobRole.objects.get(pk=job_id)

        #   Here we get the all projects that was sent for us
        projects_ids = validated_data.data.pop('projects', None)
        #  getting all prjects in the list with the in
        projects = Project.objects.filter(id__in=projects_ids)

        #   creatting the naver with the values in JSON
        naver = Naver.objects.create(**validated_data.data)

        #   Setting the JobRole in the new naver
        #   After search the objects we setting the value in the new Reference
        naver.job_role = job
        naver.save()

        #   Add one by one projects that naver relation
        [naver.projects.add(p) for p in projects]

        return Response(NaverSerializer(naver).data)


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


class JobViewSet(ModelViewSet):
    serializer_class = JobSerializer

    def get_queryset(self):
        return JobRole.objects.all()
