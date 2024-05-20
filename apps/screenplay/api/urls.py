from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.screenplay.api.views import (
    FilmScriptModelViewSet,
    HistoricSceneModelViewSet,
    SceneModelViewSet
)

router = DefaultRouter()

router.register("filmscript", FilmScriptModelViewSet, basename="filmscript")
router.register("SceneModelViewSet", SceneModelViewSet, basename="scene")
router.register("HistoricSceneModelViewSet", HistoricSceneModelViewSet, basename="historicscene")

urlpatterns = [
    path("", include(router.urls)),
]
