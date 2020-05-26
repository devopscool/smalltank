"""
Use these function to conver plain text into HTML
"""
from django.utils.html import linebreaks


def html_format(value):
    """
    Return the HTML by format argument of the value
    """
    if not value:
        return ''
    elif '</p>' not in value:
        return linebreaks(value)