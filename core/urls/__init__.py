from django.urls import path, include

app_name = 'core'

index_patterns = [
    path('', include('core.urls.archives')),
    path('categories/', include('core.urls.categories')),
]

archive_patterns = (index_patterns) # can add new pattern into this tuple

urlpatterns = archive_patterns
