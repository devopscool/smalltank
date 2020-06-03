from django.template import Library
from core.models.entry import Entry
from core.models.category import Category

register = Library()


@register.inclusion_tag('core/tags/swap.html')
def get_featured_entries(number=5, template='core/tags/content.html'):
    """
    Return the featured entries.
    """
    return {'template': template,
            'content': Entry.published.all()[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_left_popular_post(number=4, template='core/tags/left_popular.html'):
    """
    Return the left popular part entries
    """
    return {'template': template,
            'popular_content': Entry.published.filter(categories__title='python')[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_left_middle_post(number=4, template='core/tags/left_middle_post.html'):
    """
    Return the left middle post entries
    """
    return {'template': template,
            'middle_post': Entry.published.filter(categories__title='travel', is_watch_post=0)[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_left_watch_post(number=4, template='core/tags/left_middle_watch.html'):
    """
    Return the left middle post entries
    """
    return {'template': template,
            'watch_posts': Entry.published.filter(categories__title='travel', is_watch_post=1)[:number]}