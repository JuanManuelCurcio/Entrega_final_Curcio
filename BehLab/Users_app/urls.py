from django.urls import path
from .views import register_view, edit_user_view, login_view, logout_view, add_avatar_view
from django.urls import include

urlpatterns = [  
    path("register_view/", register_view, name="register_view"),
    path("login_view/", login_view, name="login_view"),
    path("edit_user_view/", edit_user_view, name="edit_user_view"),
    path("logout_view/", logout_view, name="logout_view"),
    path("add_avatar_view/", add_avatar_view, name="add_avatar_view"),
]