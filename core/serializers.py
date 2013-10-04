from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import Favorite


class FavoriteSerializer(serializers.HyperlinkedModelSerializer):

    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('id', 'content', 'description', 'owner', 'created')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    favorites = serializers.HyperlinkedRelatedField(many=True, view_name='favorite-detail', lookup_field='username')

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'favorites')
        lookup_field = 'username'