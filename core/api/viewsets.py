# framework imports
from rest_framework.viewsets import ModelViewSet

# my imported models
from core.models import Naver
from .serializers import NaverSerializer


class NaverViewSet(ModelViewSet):
    """
        Viewset that represents the naver access
    """
    queryset = Naver.objects.all()
    serializer_class = NaverSerializer
