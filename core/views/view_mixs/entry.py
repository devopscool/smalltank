from django.views.generic.base import TemplateResponseMixin


class EntryMixin(object):
    allow_future = True
    allow_empty = True
    date_field = 'publication_date'


class EntryQuerysetArchiveTemplateResponseMixin(TemplateResponseMixin):

    def get_template_names(self):
        templates = []
        template_name = 'core/entry_index.html'
        templates.append(template_name)

        return templates


class EntryQuerysetTemplateResponseMixin(TemplateResponseMixin):
    """
    Return a custom template name for views, a queryset
    of the entry filtered by other model.
    """
    def get_template_names(self):
        """
        Return a template name for the view
        """
        templates = [
            'core/category_list_detail.html']

        if self.template_name is not None:
            templates.insert(0, self.template_name)

        return templates
