from django.urls import path

from backend.apps.screenplay.api import views

urlpatterns = [
    path("film-script/create/", views.CreateFilmScriptView.as_view()),
    path("film-script/update/<int:film_script_id>/", views.UpdateFilmScriptView.as_view()),
    path("film-script/", views.ListMyFilmScriptsView.as_view()),
    path("film-script/shared/", views.ListSharedFilmScriptsView.as_view()),
    path("film-script/<int:film_script_id>/scene/", views.ListSceneView.as_view()),
    path("scene/create/", views.CreateSceneView.as_view()),
    path("scene/update/<int:scene_id>/", views.UpdateSceneView.as_view()),
    path("historic-scene/create/", views.CreateHistoricSceneView.as_view()),
    path("historic-scene/<int:scene_id>/", views.ListHistoricSceneView.as_view()),
]
