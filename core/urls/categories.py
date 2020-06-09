"""Urls for categories"""
from django.urls import path

from core.views.categories import CategoryList

urlpatterns = [
    path(r'',
         CategoryList.as_view(),
         name='category_list'),
]