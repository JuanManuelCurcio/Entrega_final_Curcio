from django.contrib import admin
from django.urls import path, include
from .views import forum_view, forum_view_access
from .views import *
 
urlpatterns = [
    path('forum_view/',forum_view,name='forum_view'),
    path('addInForum/',addInForum,name='addInForum'),
    path('addInDiscussion/',addInDiscussion,name='addInDiscussion'),
    path('forum_view_access/',forum_view_access,name='forum_view_access'),
]