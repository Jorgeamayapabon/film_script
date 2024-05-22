from typing import List

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import (
    viewsets,
    generics,
    authentication,
    permissions,
)
from rest_framework.response import Response

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
from apps.user.models import UserAccountRel


class CreateFilmScriptView(generics.CreateAPIView):
    serializer_class = FilmScriptModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UpdateFilmScriptView(generics.UpdateAPIView):
    serializer_class = FilmScriptModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListMyFilmScriptsView(generics.ListAPIView):
    serializer_class = FilmScriptModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return FilmScriptModel.objects.filter(
            owner_id=self.request.user.id
        ).all()


class ListSharedFilmScriptsView(generics.ListAPIView):
    serializer_class = FilmScriptModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_account_rels: List[UserAccountRel] = self.request.user.user_account_rel.exclude(
            user_type="Owner"
        )

        queryset = [
            user_account_rel.account.filmscript_account.get()
            for user_account_rel in user_account_rels
        ]

        serializer = FilmScriptModelSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateSceneView(generics.CreateAPIView):
    serializer_class = SceneModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UpdateSceneView(generics.UpdateAPIView):
    serializer_class = SceneModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListSceneView(generics.ListAPIView):
    serializer_class = SceneModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        film_script = FilmScriptModel.objects.get(
            id=self.kwargs["film_script_id"]
        )
        queryset = SceneModel.objects.filter(
            film_script=film_script
        ).all()
        serializer = SceneModelSerializer(queryset, many=True)
        return Response(serializer.data)
        # return queryset

    # def get_queryset(self):
    #     return SceneModel.objects.filter(
    #         film_script__owner=self.request.user.id
    #     ).all()


class CreateHistoricSceneView(generics.CreateAPIView):
    serializer_class = HistoricSceneModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListHistoricSceneView(generics.ListAPIView):
    serializer_class = HistoricSceneModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = HistoricSceneModel.objects.filter(
            id=self.kwargs["scene_id"]
        ).all()
        serializer = HistoricSceneModelSerializer(queryset, many=True)
        return Response(serializer.data)
