from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('screenplay/', include("apps.screenplay.urls"), name="screenplay"),
    path('user/', include("apps.user.urls"), name="user"),
]
