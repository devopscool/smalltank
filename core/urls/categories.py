"""Urls for categories"""
from django.urls import path, re_path

from core.views.categories import CategoryList
from core.views.categories import CategoryListDetail

urlpatterns = [
    path('',
         CategoryList.as_view(),
         name='category_list'),
    re_path(r'(?P<path>[-\/\w]+)/$',
            CategoryListDetail.as_view(),
            name='categories list detail'
            ),
]