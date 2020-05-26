from django.contrib import admin


class EntryAdmin(admin.ModelAdmin):
    """
    Admin model for the entry object
    """
    fieldsets = (
        ('Content', {
           'fields': (('title', 'status'), 'content')
        }),
        ('Illustration', {
            'fields': ('image', 'image_caption'),
            'classes': ('collapse', 'collapse-closed')
        }),
        ('Publication', {
            'fields': ('publication_date', ('start_publication', 'end_publication')),
            'classes': ('collapse', 'collapse-closed')
        }),
        (None, {'fields': ('categories', 'authors', 'slug',)}),
    )
    date_hierarchy = 'publication_date'
    list_filter = ('publication_date', 'status')
    list_display = ('get_title', 'slug')
    filter_horizontal = ('categories', 'authors', )
    search_fields = ('title', )

    def get_title(self, entry):
        """
        Return the title and wrap it with count and comments
        """
        title = '%(title)s (%(word_count)i words)' % {'title': entry.title,
                                                     'word_count': entry.word_count_report}

        return title
