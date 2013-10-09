from django.db import models

from model_utils.models import TimeStampedModel


class Favorite(TimeStampedModel):
    """
    This is the model related with django user
    """
    owner = models.ForeignKey('auth.User', related_name='favorites')
    content = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.content