from django.urls import path

from core.views.archives import EntryIndex

urlpatterns = [
    path('',
        EntryIndex.as_view(),
        name='entry_index_archive'),
]