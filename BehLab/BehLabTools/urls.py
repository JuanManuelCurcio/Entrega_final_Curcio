from django.urls import path
from django.urls import include
from .views import BehLabTools_view

urlpatterns = [  
path('BehLabTools_view', BehLabTools_view, name='BehLabTools_view')
]