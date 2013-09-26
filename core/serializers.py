from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from core.models import Favorite


class FavoriteSerializer(serializers.Serializer):

    pk = serializers.Field()  # Note: `Field` is an untyped read-only field.
    url = serializers.CharField(required=False, max_length=1000)
    description = serializers.CharField(required=False, max_length=1000)
    owner = serializers.Field(source='owner.username')
    created = serializers.DateTimeField(required=False)

    def restore_object(self, attrs, instance=None):
        """
        Create or update a new snippet instance, given a dictionary
        of deserialized field values.

        Note that if we don't define this method, then deserializing
        data will simply return a dictionary of items.
        """
        if instance:
            # Update existing instance
            instance.title = attrs.get('url', instance.url)
            instance.description = attrs.get('code', instance.description)
            return instance

        # Create new instance
        return Favorite(**attrs)


class UserSerializer(serializers.ModelSerializer):
    favorites = FavoriteSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'favorites')