# framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

#django shortcut
from django.shortcuts import get_object_or_404

# my imported models
from core.models import Naver
from core.api.query_string import NaversFilters
from core.api.serializers import *


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
        print(self.action)
        if self.action == 'retrieve':
            return DetailNaverSerializer
        else:
            return NaverSerializer