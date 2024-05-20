from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('screenplay/', include("apps.screenplay.urls")),
    path('user/', include("apps.user.urls")),
]
