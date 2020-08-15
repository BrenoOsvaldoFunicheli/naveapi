#   import models of the auth django's package
from django.contrib.auth.models import User, Group

#   rest frameworks's response
from rest_framework import viewsets, permissions
from rest_framework.response import Response  

#   my serializers classes 
from users.api.serializers import UserSerializer

unavailable_resource = Response({"result":"this resource isn't available"})

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, pk=None):
        return unavailable_resource

    def destroy(self, request, *args, **kwargs):
        return unavailable_resource

    def update(self, request, *args, **kwargs):
        return unavailable_resource

    def partial_update(self, request, *args, **kwargs):
        return unavailable_resource

