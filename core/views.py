from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from core.models import Favorite
from core.serializers import FavoriteSerializer, UserSerializer
from core.permissions import IsOwnerOrReadOnly, IsUser


class FavoriteList(generics.ListCreateAPIView):
    """
    List all favorites
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    List only authenticated user's favorites
    """
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user


class UserList(generics.ListAPIView):
    """
    List all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    """
    List only authenticated user's details with favorites
    """
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsUser,)


@api_view(('GET',))
def api_root(request, format=None):
    """
    Bring together all urls
    """
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'favorites': reverse('favorite-list', request=request, format=format)
    })