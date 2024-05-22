from django.contrib import admin

from backend.apps.user.models import (
    AccountModel,
    User
)


@admin.register(User)
class UserScripterAdmin(admin.ModelAdmin):
    # readonly_fields = ("id", "owner", "account")
    list_display = [
        "id", 
        "name", 
        "email",
    ]
    search_fields = ["name"]
    

@admin.register(AccountModel)
class AccountAdmin(admin.ModelAdmin):
    # readonly_fields = ("id", "owner", "account")
    list_display = [
        "id", 
        "uuid", 
        "name",
    ]
    search_fields = ["name"]
