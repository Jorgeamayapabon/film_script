from django.urls import path, include

from apps.user.api import urls as api_urls

urlpatterns = [
    path(
        '',
        include(api_urls.urlpatterns)
    ),
]
