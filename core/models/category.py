""" Category model for smalltank """
from django.db import models

from core.managers import EntryPublishedManager

from mptt.managers import TreeManager
from mptt.models import MPTTModel
from mptt.models import TreeForeignKey


class Category(MPTTModel):
    """
    The category model for entries
    """

    title = models.CharField(
        'title', max_length=255)

    slug = models.SlugField(
        'slug', unique=True, max_length=255,
        help_text='cagegory slug')

    parent = TreeForeignKey('self',
                            related_name='children',
                            null=True, blank=True,
                            on_delete=models.SET_NULL,
                            verbose_name='parent category')

    description = models.TextField(
        'description', blank=True)

    # object = TreeManager()
    # published = EntryPublishedManager()

    @property
    def category_tree_path(self):
        """
        Return category's tree path info
        """
        if self.parent_id:
            return '/'.join(
                [ancestor.slug for ancestor in self.get_ancestors()] + [self.slug]
            )
        return self.slug

    def __str__(self):
        return self.title

    class Meta:
        """
        Category Meta
        """
        ordering = ['title']
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    class MPTTMeta:
        """
        MPTT's meta setting
        """
        order_insertion_by = ['title']