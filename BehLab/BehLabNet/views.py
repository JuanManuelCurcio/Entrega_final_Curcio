from django.shortcuts import render
from django.shortcuts import redirect
from .forms import NewProyectForm
from .views import Proyects


# Create your views here.
def BehLabNet_view(req):
    if req.user.is_authenticated:
        return render(req, "BehLabNet_view.html", {})
    else:
        return redirect('no_access_view')
    
def search_proyect_view(req):
    return render(req, "search_proyect_view.html")

def result_proyect_view(req):
    return render(req, "result_proyect_view.html")


# ADD PROYECT

def NewProyectForm_view(req):
    if req.method == 'POST':
        form_new_proyect = NewProyectForm(req.POST)

        if form_new_proyect.is_valid():  
            new_proyect = Proyects(
                user=req.user,
                name_proyect=form_new_proyect.cleaned_data["nombre_proyecto"],
                brief_description=form_new_proyect.cleaned_data["breve_descripcion"],
            )
            new_proyect.save()  
            return render(req, "proyect_uploaded.html", {})  
    else:
        form_new_proyect = NewProyectForm()  

    return render(req, "NewProyectForm_view.html", {"form_new_proyect": form_new_proyect})