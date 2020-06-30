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
            'middle_post': Entry.published.filter(
                categories__title='travel',
                is_watch_post=0)[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_left_watch_post(number=4, template='core/tags/left_middle_watch.html'):
    """
    Return the left middle post entries
    """
    return {'template': template,
            'watch_posts': Entry.published.filter(
                categories__title='travel',
                is_watch_post=1)[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_left_under_post(number=4, template='core/tags/left_under_post.html'):
    """
    Return the left middle post entries
    """
    return {'template': template,
            'letf_under_posts': Entry.published.filter(
                categories__title='fashion')[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_carousel(number=3, template='core/tags/carousel_panel.html'):
    """
    Return the left middle post entries
    """
    return {'template': template,
            'entry_carousel': Entry.published.filter(
                is_carousel_post=1)[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_news_area(number=3, template='core/tags/news_area.html'):
    """
    Return the entries of news
    """
    a = {'template': template,
            'entry_news': Entry.published.filter(
                as_news=1)[:number]}

    return {'template': template,
            'entry_news': Entry.published.filter(
                as_news=1)[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_top_header(template='core/tags/top_header.html'):
    """
    Return the left middle post entries
    """
    return {'template': template}


@register.inclusion_tag('core/tags/swap.html')
def get_main_header(template='core/tags/main_header.html'):
    """
    Return the left middle post entries
    """
    return {'template': template}


@register.inclusion_tag('core/tags/swap.html')
def get_breadcrumb(template='core/tags/breadcrumb.html'):
    """
    Return the left middle post entries
    """
    return {'template': template}


@register.inclusion_tag('core/tags/swap.html')
def get_news_left_sidebar(number=3, template='core/tags/news_left_sidebar.html'):
    """
    Return the left side html code of news list
    """
    return {'template': template,
            'entry_list': Entry.published.filter(
                as_news=1)[:number]}


@register.inclusion_tag('core/tags/swap.html')
def get_news_right_sidebar(number=3, template='core/tags/news_right_sidebar.html'):
    """
    Return the right side html code of news list
    """
    return {'template': template}


@register.inclusion_tag('core/tags/swap.html')
def get_connect_us(number=3, template='core/tags/get_connect_us.html'):
    """
    Return the connect us html code
    """
    return {'template': template}


@register.inclusion_tag('core/tags/swap.html')
def get_foot_area(number=3, template='core/tags/foot_area.html'):
    """
    Return the connect us html code
    """
    return {'template': template}