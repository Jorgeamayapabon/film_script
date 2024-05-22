from rest_framework import serializers

from apps.screenplay.models import FilmScriptModel, HistoricSceneModel, SceneModel


class FilmScriptModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilmScriptModel
        fields = "__all__"

    def create(self, validate_data):
        return FilmScriptModel.objects.create(**validate_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.pop("title", instance.title)
        instance.genre = validate_data.pop("genre", instance.genre)
        instance.save()
        return instance


class SceneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SceneModel
        fields = "__all__"

    def create(self, validate_data):
        return SceneModel.objects.create(**validate_data)

    def update(self, instance: SceneModel, validate_data):
        instance.film_script = validate_data.get("film_script", instance.film_script)
        instance.name = validate_data.get("name", instance.name)
        instance.actor_name = validate_data.get("actor_name", instance.actor_name)
        instance.actor_location = validate_data.get("actor_location", instance.actor_location)
        instance.actor_gesture = validate_data.get("actor_gesture", instance.actor_gesture)
        instance.dialogue = validate_data.get("dialogue", instance.dialogue)
        instance.save()
        return instance


class HistoricSceneModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricSceneModel
        fields = "__all__"

    def create(self, validate_data):
        return HistoricSceneModel.objects.create(**validate_data)
