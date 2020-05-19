""" The admin code of smalltank"""
from django.contrib import admin

from core.models.entry import Entry
from core.admin.entry import EntryAdmin

admin.site.register(Entry, EntryAdmin)