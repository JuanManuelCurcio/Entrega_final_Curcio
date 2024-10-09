from django.shortcuts import render
from django.shortcuts import redirect
import pandas as pd
from django.shortcuts import render
from .forms import csv_upload_form
from io import TextIOWrapper # para manejar in-out: https://docs.python.org/es/3.10/library/io.html


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
