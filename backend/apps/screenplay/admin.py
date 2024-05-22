from django.contrib import admin

from backend.apps.screenplay.models import (
    FilmScriptModel,
    HistoricSceneModel,
    SceneModel
)


@admin.register(FilmScriptModel)
class FilmScriptAdmin(admin.ModelAdmin):
    # readonly_fields = ("id", "owner", "account")
    list_display = [
        "id", 
        "owner", 
        "account", 
        "title", 
        "genre"
    ]
    search_fields = ["name"]
    

@admin.register(SceneModel)
class SceneAdmin(admin.ModelAdmin):
    # readonly_fields = ("id", "film_script", "created_by", "updated_by")
    list_display = [
        "id", 
        "film_script", 
        "name", 
        "actor_name", 
        "actor_location",
        "actor_gesture",
        "created_by",
        "updated_by"
    ]
    search_fields = ["name"]


@admin.register(HistoricSceneModel)
class HistoricSceneAdmin(admin.ModelAdmin):
    # readonly_fields = ("id", "scene", "updated_by", "update_at")
    list_display = [
        "id", 
        "scene",
        "updated_by",
        "update_at"
    ]
    search_fields = ["scene"]
