from typing import List

from rest_framework import (
    generics,
    authentication,
    permissions,
)
from rest_framework.response import Response

from backend.apps.screenplay.api.serializer import (
    FilmScriptModelSerializer,
    HistoricSceneModelSerializer,
    SceneModelSerializer
)
from backend.apps.screenplay.models import (
    FilmScriptModel,
    HistoricSceneModel,
    SceneModel
)
from backend.apps.user.models import UserAccountRel


class CreateFilmScriptView(generics.CreateAPIView):
    serializer_class = FilmScriptModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class UpdateFilmScriptView(generics.UpdateAPIView):
    serializer_class = FilmScriptModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    queryset = FilmScriptModel.objects.all()

    def partial_update(self, request, *args, **kwargs):
        film_script = FilmScriptModel.objects.get(id=self.kwargs["film_script_id"])
        account = film_script.account

        user_account_rel: UserAccountRel = self.request.user.user_account_rel.filter(
            account=account
        ).first()

        if (
                user_account_rel.user_type == "Owner"
                or user_account_rel.user_type == "Screenwriter"
        ):
            # Obtener el serializador con la instancia existente y los datos nuevos
            serializer = self.get_serializer(film_script, data=request.data, partial=True)

            # Validar los datos
            serializer.is_valid(raise_exception=True)

            # Guardar los cambios
            self.perform_update(serializer)

            # Devolver la respuesta con los datos actualizados
            return Response(serializer.data, status=200)
        return Response(
            status=403,
            data={"Error": "You do not have permissions to modify the scene"}
        )


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
    queryset = SceneModel.objects.all()

    def partial_update(self, request, *args, **kwargs):
        scene = SceneModel.objects.get(id=self.kwargs["scene_id"])
        account = scene.film_script.account

        user_account_rel: UserAccountRel = self.request.user.user_account_rel.filter(
            account=account
        ).first()

        if (
            user_account_rel.user_type == "Owner"
            or user_account_rel.user_type == "Screenwriter"
        ):
            # Obtener el serializador con la instancia existente y los datos nuevos
            serializer = self.get_serializer(scene, data=request.data, partial=True)

            # Validar los datos
            serializer.is_valid(raise_exception=True)

            # Guardar los cambios
            self.perform_update(serializer)

            # Devolver la respuesta con los datos actualizados
            return Response(serializer.data, status=200)
        return Response(
            status=403,
            data={"Error": "You do not have permissions to modify the scene"}
        )


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
