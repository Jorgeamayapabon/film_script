from django.urls import path
from apps.user.api import views

urlpatterns = [
    path("signup/", views.CreateUserView.as_view()),
    path("signin/", views.CreateTokenView.as_view()),
    path("user/", views.RetrieveUpdateUserView.as_view()),
    path("account/create/", views.CreateAccountView.as_view()),
    path("account/", views.ListMyAccountView.as_view()),
    path("account/shared/", views.ListSharedAccountView.as_view()),
    path("user-account-rel/", views.CreateUserAccountRelView.as_view()),
]
