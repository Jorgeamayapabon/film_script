from django.urls import path, include

from apps.screenplay.api import urls as api_urls

urlpatterns = [
    path(
        'api/',
        include(api_urls.urlpatterns)
    ),
]
