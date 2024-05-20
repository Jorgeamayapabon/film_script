from rest_framework import viewsets

from apps.user.api.serializer import (
    AccountModelSerializer,
    UserAccountRelSerializer,
    UserSerializer
)
from apps.user.models import (
    AccountModel,
    UserAccountRel,
    UserModel
)

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer


class AccountModelViewSet(viewsets.ModelViewSet):
    queryset = AccountModel.objects.all()
    serializer_class = AccountModelSerializer


class UserAccountRelViewSet(viewsets.ModelViewSet):
    queryset = UserAccountRel.objects.all()
    serializer_class = UserAccountRelSerializer
