# framework imports
from rest_framework.viewsets import ModelViewSet

# my imported models
from core.models import Naver
from core.api.query_string import NaversFilters
from .serializers import NaverSerializer


class NaverViewSet(ModelViewSet):
    """
        Viewset that represents the naver access
    """

    serializer_class = NaverSerializer

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
