"""The category admin for smalltank"""
from django.contrib import admin
from django.utils.html import format_html


class CategoryAdmin(admin.ModelAdmin):
    """
    The category model's admin part
    """
    fields = ('title', 'parent', 'description', 'slug')
    search_fields = ('title', 'description')
    list_filter = ('parent',)
    # prepopulated_fields = {'slug': ('title', )}
    list_display = ('title', 'slug', 'get_parent_tree_and_path', 'description')

    def get_parent_tree_and_path(self, category):
        """
        Display the category tree path in admin page.
        """

        # this strings need convert to html element
        # and have the category's href url.
        return '/%s/' % category.category_tree_path

    get_parent_tree_and_path.short_description = 'cagegory path'
