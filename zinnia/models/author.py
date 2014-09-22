"""Author model for Zinnia"""
from django.db import models
from django.conf import settings

from zinnia.managers import entries_published
from zinnia.managers import EntryRelatedPublishedManager


class Author(models.Model):
    """
    A concrete model linked to :class:`django.contrib.auth.models.get_user_model`.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    objects = models.Manager()
    published = EntryRelatedPublishedManager()

    def entries_published(self):
        """
        Returns author's published entries.
        """
        return entries_published(self.entries)

    @models.permalink
    def get_absolute_url(self):
        """
        Builds and returns the author's URL based on his username.
        """
        return ('zinnia:author_detail', [self.user.get_username()])

    def __str__(self):
        """
        If the user has a full name, use it instead of the username.
        """
        return self.user.get_full_name() or self.user.get_username()

    class Meta:
        """
        Author's meta informations.
        """
        app_label = 'zinnia'