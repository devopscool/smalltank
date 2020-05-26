from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
from django.utils.html import strip_tags

from core.managers import EntryPublishedManager
from core.setting import UPLOAD_DEST
from core.markups import html_format

import os


class BaseEntry(models.Model):
    """
    Abstract entry model class providing
    the main fields and methods for content
    publishing.
    """
    STATUS_CHOICES = ((0, 'draft'),
                      (1, 'hidden'),
                      (2, 'published'))

    title = models.CharField('title', max_length=255)
    slug = models.SlugField(
        'slug', max_length=255,
        unique_for_date='publication_date',
        help_text="Used to build the entry's URL."
    )
    status = models.IntegerField(
        'status', db_index=True,
        choices=STATUS_CHOICES, default=0
    )

    publication_date = models.DateTimeField(
        'publication date',
        db_index=True, default=timezone.now,
        help_text="Used to build the entry's URL.")

    start_publication = models.DateTimeField('start publication', db_index=True, blank=True, null=True,
                                             help_text='Start date of publication')

    end_publication = models.DateTimeField('end of publication', db_index=True, blank=True, null=True,
                                           help_text='End date of publication')

    create_date = models.DateTimeField(
        'create date', default=timezone.now())

    last_update = models.DateTimeField(
        'last update date', default=timezone.now())

    object = models.Manager()
    published = EntryPublishedManager()

    class Meta:
        """
        base entry meta info
        """
        abstract = True
        ordering = ['-publication_date']
        get_latest_by = 'publication_date'
        verbose_name = 'entry'
        verbose_name_plural = 'entries'
        # index_together = []
        permissions = (('can_view_all', 'Can view all entries'),
                       ('can_change_status', 'Can change status'),
                       ('can_change_author', 'Can change authors(s)'))


class ContentEntry(models.Model):
    """
    Abstract content model class defined fields and methods
    """
    content = models.TextField('content', blank=True)

    @property
    def html_content(self) -> str:
        """
        Return the content with the `html_format`
        """
        return html_format(self.content)

    @property
    def word_count_report(self) -> int:
        """
        Count the number of the words in content
        """
        return len(strip_tags(html_format(self.html_content)).split())

    class Meta:
        abstract = True


def image_upload_dispatcher(entry: str, filename: str) -> str:
    """
    Overriding of `` image_update `` method
    :param entry: the instance entry
    :param filename: the upload file's name
    :return: the file's path
    """
    return entry.image_update(filename)


class ImageEntry(models.Model):
    """
    Abstract image model class defined fields and methods
    """
    def image_update(self, filename):
        now = timezone.now()
        filename, extension = os.path.splitext(filename)

        return os.path.join(
            UPLOAD_DEST,
            now.strftime('%Y'),
            now.strftime('%m'),
            now.strftime('%d'),
            '%s%s' % (slugify(filename), extension)
        )

    image = models.ImageField(
        'image', blank=True, upload_to=image_upload_dispatcher, help_text='Used to the illustration part'
    )

    image_caption = models.TextField('caption', blank=True, help_text="The image's caption")

    class Meta:
        abstract = True


class CategoryEntry(models.Model):
    """
    Abstract model class for entries categorized
    """
    categories = models.ManyToManyField('core.Category',
                                        blank=True,
                                        related_name='entries',
                                        verbose_name='categories')

    class Meta:
        abstract = True


class AuthorsEntry(models.Model):
    """
    Abstract model class about the relationship between entries and their authors
    """
    authors = models.ManyToManyField(
        'core.Author',
        blank=True,
        related_name='entries',
        verbose_name='authors')

    class Meta:
        abstract = True

# class AuthorsInfoEntry(models.Model):
#     """
#     Abstract model class for the relationship of entries and their authors
#     """
    # authors = models.ManyToManyField('smalltank.Author',
    #                                  blank=True,
    #                                  related_name='entries',
    #                                  verbose_name='authors')


class AbstractEntry(
        BaseEntry,
        ContentEntry,
        ImageEntry,
        CategoryEntry,
        AuthorsEntry):
    """
    abstract entry model class assembling
    all the abstract entry model in this class

    In this manner we can override some fields without
    reimplement all the Abstract Entries.
    """

    class Meta(BaseEntry.Meta):
        abstract = True