""" Authors model for smalltank """
from django.apps import apps
from django.conf import settings
from django.db import models

from core.managers import EntryPublishedManager


def safe_user_model():
    """
    Safe get the User model
    """
    auth_app, user_model = settings.AUTH_USER_MODEL.split('.')
    return apps.get_registered_model(auth_app, user_model)


class AuthorPublishedManager(models.Model):
    """
    Proxy model manager for author
    """
    published = EntryPublishedManager()

    class Meta:
        abstract = True


class Author(safe_user_model(), AuthorPublishedManager):
    """
    Proxy model for Users, to: class `django.contrib.auth.models.get_user_model`
    """
    def __str__(self):
        """
        Return a user name
        """
        return (self.get_short_name()
                or self.get_full_name()
                or self.get_username())

    class Meta:
        """
        Author's meta info
        """
        proxy = True
