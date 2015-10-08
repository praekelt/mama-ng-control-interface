from django.contrib.auth.models import User, Group
from .models import DummyModel
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import (UserSerializer, GroupSerializer,
                          DummyModelSerializer)


class UserViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class DummyModelViewSet(viewsets.ModelViewSet):

    """
    API endpoint that allows dummy models to be viewed or edited.
    """
    permission_classes = (IsAuthenticated,)
    queryset = DummyModel.objects.all()
    serializer_class = DummyModelSerializer