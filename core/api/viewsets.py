#   framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser

#   django filters implementation
from django_filters.rest_framework import DjangoFilterBackend

#   django shortcut
from django.shortcuts import get_object_or_404

#   my imported models
from core.models import Naver, Project, JobRole, Technologie
from core.api.query_string import NaversFilters
from core.api.serializers import *

#   jwt import
from rest_framework.permissions import IsAuthenticated


class NaverViewSet(ModelViewSet):
    """
        Viewset that represents the naver access
    """

    permission_classes = (IsAuthenticated, )

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

        user = self.request.user

        n_filter = NaversFilters(user, params)
        return n_filter.get_objects()

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

        #   After search the objects we setting the value in the new Reference
        naver.job_role = job  # Setting the JobRole in the new naver

        #   Add one by one projects that naver relation
        [naver.projects.add(p) for p in projects]

        #   Add creator for new naver
        naver.creator = validated_data.user
        naver.save()

        return Response(NaverSerializer(naver).data)


class ProjectViewSet(ModelViewSet):
    """
        Class to handle the serializer and data
        that show as Endpoint handler  
    """
    permission_classes = (IsAuthenticated, )
    serializer_class = ProjectSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', )

    def get_queryset(self):
        return Project.objects.filter(creator=self.request.user.id)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DetailProjectSerializer
        else:
            return ProjectSerializer

    def create(self, validated_data):
        """
            Parameters
            ----------

                Send just JSON objects because the django will be get
                the Immutable QueryDict when you send the form-data, 
                and when you will get objects with the pop method you'll 
                get the error in the API Endpoint. 
        """
        tecnologies_ids = validated_data.data.pop('tecnologies', None)
        tecnologies = Technologie.objects.filter(id__in=tecnologies_ids)

        #   Here we get the all projects that was sent for us
        navers_ids = validated_data.data.pop('navers', None)
        #   getting all projects in the list with the in operator
        navers = Naver.objects.filter(id__in=navers_ids)

        #   creatting the project with the values in JSON
        project = Project.objects.create(**validated_data.data)

        #   Add one by one the tecnologies that this will be project relation
        [project.tecnologies.add(t) for t in tecnologies]

        #   Add one by one the navers that this will be project relation
        [project.naver_set.add(n) for n in navers]

        #   Add creator for new project
        project.creator = validated_data.user

        project.save()

        return Response(ProjectSerializer(project).data)


class JobViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated, )
    serializer_class = JobSerializer

    def get_queryset(self):
        return JobRole.objects.all()


class TecnologiesViewSet(ModelViewSet):

    permission_classes = (IsAuthenticated, )
    serializer_class = JobSerializer

    def get_queryset(self):
        return Technologie.objects.all()
