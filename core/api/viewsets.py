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
    # queryset = Naver.objects.all()
    serializer_class = NaverSerializer

    def get_queryset(self):
        params = self.request.query_params
        n_filter = NaversFilters(params)
        return n_filter.get_objects()
