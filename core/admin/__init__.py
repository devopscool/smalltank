""" The admin code of smalltank"""
from django.contrib import admin

from core.models.entry import Entry
from core.models.category import Category
from core.admin.entry import EntryAdmin
from core.admin.category import CategoryAdmin

admin.site.register(Entry, EntryAdmin)
admin.site.register(Category, CategoryAdmin)