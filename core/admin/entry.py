from django.contrib import admin


class EntryAdmin(admin.ModelAdmin):
    """
    Admin model for the entry object
    """
    date_hierarchy = 'publication_date'
    list_filter = ('publication_date', 'status')
    list_display = ('title', 'slug')
    search_fields = ('title', )

    def get_title(self, entry):
        """
        Return the title and wrap it with count and comments
        """
        title = '%(title)s (%(word_count)i words' % {'title': entry.title, 'word_count': entry.word__count}
