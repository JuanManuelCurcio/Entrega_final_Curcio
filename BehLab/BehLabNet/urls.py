from django.contrib import admin
from django.urls import path
from .views import BehLabNet_view, result_proyect_view, NewProyectForm_view, search_proyect_view
 
urlpatterns = [
    path('BehLabNet_view/',BehLabNet_view,name='BehLabNet_view'),
    path('result_proyect_view/',result_proyect_view,name='result_proyect_view'),
    path('NewProyectForm_view/',NewProyectForm_view,name='NewProyectForm_view'),
    path('search_proyect_view/',search_proyect_view,name='search_proyect_view'),
]