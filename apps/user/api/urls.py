from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.user.api.views import (
    AccountModelViewSet,
    UserAccountRelViewSet, 
    UserModelViewSet
)


router = DefaultRouter()

router.register("user", UserModelViewSet, basename="user")
router.register("account", AccountModelViewSet, basename="account")
router.register("user_account_rel", UserAccountRelViewSet, basename="user_account_rel")

urlpatterns = [
    path("", include(router.urls)),
]
