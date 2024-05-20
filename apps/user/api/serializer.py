from rest_framework import serializers

from apps.user.models import (
    AccountModel,
    UserAccountRel,
    UserModel
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = "__all__"


class AccountModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountModel
        fields = "__all__"


class UserAccountRelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccountRel
        fields = "__all__"
