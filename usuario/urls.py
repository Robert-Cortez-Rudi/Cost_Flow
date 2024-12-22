from django.urls import path
from usuario.views import home, login, register, logout, profile, edit_profile

urlpatterns = [
    path("", home, name="home"),
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("profile/edit/", edit_profile, name="edit_profile")
]
