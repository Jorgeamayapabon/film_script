from django.contrib import admin

from apps.user.models import (
    AccountModel,
    UserModel
)


@admin.register(UserModel)
class UserScripterAdmin(admin.ModelAdmin):
    # readonly_fields = ("id", "owner", "account")
    list_display = [
        "id", 
        "fullname", 
        "email",
    ]
    search_fields = ["fullname"]
    

@admin.register(AccountModel)
class AccountAdmin(admin.ModelAdmin):
    # readonly_fields = ("id", "owner", "account")
    list_display = [
        "id", 
        "uuid", 
        "name",
    ]
    search_fields = ["name"]
