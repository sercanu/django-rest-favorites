from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import Favorite


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('id', 'content', 'description', 'owner', 'created')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    favorites = FavoriteSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'favorites')
        lookup_field = 'username'