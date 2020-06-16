"""views for categories"""
from django.views.generic.list import ListView
from django.db.models import Count
from django.shortcuts import get_object_or_404

from core.models.category import Category
from core.views.view_mixs.entry import EntryQuerysetTemplateResponseMixin
from core.setting import PAGINATION


def get_category_or_path_info(path):
    """
    Retrieve a Category request path
    """
    path_info = [k for k in path.split('/') if k]
    return get_object_or_404(Category, slug=path_info[-1])


class CategoryList(ListView):
    """
    Retrieve a Category object by the url path
    """

    def get_queryset(self):
        """
        Return a queryset of categories
        """
        return Category.published.all().annotate(
            count_entries_published=Count('entries'))


class BaseCategoryDetailDateQueryset(object):
    """
    Providing the behavior detail of category
    """
    def get_queryset(self):
        """
        Retrieve category with kwargs `path` and
        Return a queryset of published entries
        """
        self.category = get_category_or_path_info(self.kwargs['path'])
        return self.category.entries_published_data()


class CategoryListDetail(EntryQuerysetTemplateResponseMixin,
                         BaseCategoryDetailDateQueryset,
                         ListView):
    """
    Detail for the Category object.
    - EntryQuerysetTemplateResponseMixin provide templates
    -
    -
    -
    """
    # paginate_by = PAGINATION
