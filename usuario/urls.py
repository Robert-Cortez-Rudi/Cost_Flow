from django.urls import path
from usuario.views import home, login_user, register, logout_user, profile, edit_profile, delete_profile

urlpatterns = [
    path("", home, name="home"),
    path("login/", login_user, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout_user, name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", edit_profile, name="edit_profile"),
    path("profile/delete", delete_profile, name="delete_profile")
]
