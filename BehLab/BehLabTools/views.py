from django.shortcuts import render
from django.shortcuts import redirect
import pandas as pd
from django.shortcuts import render
from BehLab import settings
import os
from .forms import csv_upload_form
from io import TextIOWrapper # para manejar in-out: https://docs.python.org/es/3.10/library/io.html
import seaborn as sns
import matplotlib.pyplot as plt


# Create your views here.

# IF NO LOG-IN

def BehLabTools_view(req):
    if req.user.is_authenticated:
        return render(req, "BehLabTools_view.html", {})
    else:
        return redirect('no_access_view')
    

# LOAD CSV FILE, DESCRIBE


def load_csv_describe_view(req):
    if req.method == 'POST':
        form = csv_upload_form(req.POST, req.FILES)
        if form.is_valid():
            csv_file = req.FILES['csv_file']
            df = pd.read_csv(csv_file.file, sep=';',encoding='utf-8')
            results = df.describe().round(2)
            return render(req, 'results_describe.html', {'results': results.to_html(), 'csv_file': df.to_html(index=False)})
    else:
        form = csv_upload_form()

    return render(req, 'load_csv_describe_view.html', {'form': form})

# LOAD CSV FILE, CORRELATION MATRIX

def load_csv_mcorr_view(req):
    if req.method == 'POST':
        form = csv_upload_form(req.POST, req.FILES)
        if form.is_valid():
            csv_file = req.FILES['csv_file']
            df = pd.read_csv(csv_file.file, sep=';',encoding='utf-8')
            
            mcorr = df.corr(method='pearson').round(2)

            plt.figure(figsize=(12, 10))
            graf = sns.heatmap(df.corr('pearson').round(2), annot=True, cmap='magma',annot_kws={"size": 20})
            graf.set_xticklabels(graf.get_xticklabels(), rotation=45, fontsize=14)
            graf.set_yticklabels(graf.get_yticklabels(), rotation=0, fontsize=14)
            plot_dir = os.path.join(settings.MEDIA_ROOT, 'plots') # esto me conviene me parece rearlo en algun la do como fijo como el media root
            image_path = os.path.join(plot_dir, 'correlation_heatmap.png')
            plt.savefig(image_path)
            plt.close()

            return render(req, 'results_mcorr.html', {'graf': os.path.join(settings.MEDIA_URL, 'plots', 'correlation_heatmap.png'),  'mcorr': mcorr.to_html(), 
            'csv_file': df.to_html(index=False)})
    else:
        form = csv_upload_form()

    return render(req, 'load_csv_mcorr_view.html', {'form': form})