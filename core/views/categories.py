"""views for categories"""
from django.views.generic.list import ListView
from django.db.models import Count

from core.models.category import Category


class CategoryList(ListView):
    """
    Retrieve a Category object by the url path
    """

    def get_queryset(self):
        """
        Return a queryset of categories
        """
        b = Category.published.all().annotate(
            count_entries_published=Count('entries'))
        print(b)

        return Category.published.all().annotate(
            count_entries_published=Count('entries'))