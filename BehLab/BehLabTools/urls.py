from django.urls import path
from django.urls import include
from .views import BehLabTools_view, load_csv_describe_view

urlpatterns = [  
path('BehLabTools_view', BehLabTools_view, name='BehLabTools_view'),
path('load_csv_describe_view', load_csv_describe_view, name='load_csv_describe_view'), # LO IDEAL SERIA QUE SE CARGUE EL CSV Y DESPUES SE PUEDA HACER CUALQUIER COSA
]