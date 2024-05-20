from rest_framework import serializers

from apps.screenplay.models import FilmScriptModel, HistoricSceneModel, SceneModel


class FilmScriptModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmScriptModel
        fields = "__all__"


class SceneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SceneModel
        fields = "__all__"


class HistoricSceneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricSceneModel
        fields = "__all__"
