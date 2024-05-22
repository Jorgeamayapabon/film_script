from typing import List

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import (
    generics,
    authentication,
    permissions,
)
from rest_framework.response import Response

from backend.apps.user.api.serializer import (
    AccountModelSerializer,
    UserAccountRelSerializer,
    UserSerializer,
    AuthTokenSerializer
)
from backend.apps.user.models import (
    UserAccountRel
)


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    

class RetrieveUpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get_object(self):
        return self.request.user


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer


class CreateAccountView(generics.CreateAPIView):
    serializer_class = AccountModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class ListMyAccountView(generics.ListAPIView):
    serializer_class = AccountModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_account_rels: List[UserAccountRel] = self.request.user.user_account_rel.filter(
            user_type="Owner"
        ).all()
        queryset = [
            user_account_rel.account
            for user_account_rel in user_account_rels
        ]
        serializer = AccountModelSerializer(queryset, many=True)
        return Response(serializer.data)


class ListSharedAccountView(generics.ListAPIView):
    serializer_class = AccountModelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_account_rels: List[UserAccountRel] = self.request.user.user_account_rel.exclude(
            user_type="Owner"
        )
        queryset = [
            user_account_rel.account
            for user_account_rel in user_account_rels
        ]
        serializer = AccountModelSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateUserAccountRelView(generics.CreateAPIView):
    serializer_class = UserAccountRelSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
