from django.urls import path
from .views import BehLabTools_view, load_csv_describe_view, load_csv_mcorr_view, load_csv_boxplot_view

urlpatterns = [  
path('BehLabTools_view', BehLabTools_view, name='BehLabTools_view'),
path('load_csv_describe_view', load_csv_describe_view, name='load_csv_describe_view'),
path('load_csv_mcorr_view',load_csv_mcorr_view, name= 'load_csv_mcorr_view'),
path('load_csv_boxplot_view',load_csv_boxplot_view, name= 'load_csv_boxplot_view')
]