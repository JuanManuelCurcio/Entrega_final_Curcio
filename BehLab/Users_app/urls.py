from django.urls import path
from .views import *


urlpatterns = [  
    path("register_view/", register_view, name="register_view"),
    path("login_view/", login_view, name="login_view"),
    path("edit_user_view/", edit_user_view, name="edit_user_view"),
    path("logout_view/", logout_view, name="logout_view"),
    path("add_avatar_view/", add_avatar_view, name="add_avatar_view"),
    path("user_panel_view/", user_panel_view, name="user_panel_view"),
    path("user_proyects_view/", user_proyects_view, name="user_proyects_view"),
    path("detail_proyects_view/<pk>", ProyectDetail.as_view(), name="detail_proyects_view"),
    path("delete_proyects_view/<pk>", ProyectDelete.as_view(), name="delete_proyects_view"),
    path("update_proyects_view/<pk>", ProyectUpdate.as_view(), name="update_proyects_view"),
]