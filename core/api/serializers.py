from rest_framework.serializers import ModelSerializer
from core.models import Naver


class NaverSerializer(ModelSerializer):
    """
        Serializer that will be provid serialization
    """
    class Meta:
        model = Naver
        fields = ('id', 'name', 'status', 'job_role', 'admission_date')
