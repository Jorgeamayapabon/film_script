from rest_framework import viewsets
from apps.screenplay.api.serializer import (
    FilmScriptModelSerializer, 
    HistoricSceneModelSerializer, 
    SceneModelSerializer
)
from apps.screenplay.models import (
    FilmScriptModel,
    HistoricSceneModel, 
    SceneModel
)

class FilmScriptModelViewSet(viewsets.ModelViewSet):
    queryset = FilmScriptModel.objects.all()
    serializer_class = FilmScriptModelSerializer


class SceneModelViewSet(viewsets.ModelViewSet):
    queryset = SceneModel.objects.all()
    serializer_class = SceneModelSerializer


class HistoricSceneModelViewSet(viewsets.ModelViewSet):
    queryset = HistoricSceneModel.objects.all()
    serializer_class = HistoricSceneModelSerializer
