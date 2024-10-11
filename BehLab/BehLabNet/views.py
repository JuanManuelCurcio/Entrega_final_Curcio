from django.shortcuts import render
from django.shortcuts import redirect
from .forms import NewProyectForm, SearchProyectForm
from .models import Proyects


# Create your views here.
def BehLabNet_view(req):
    if req.user.is_authenticated: 
        proyects = Proyects.objects.all()
        return render(req, "BehLabNet_view.html", {
            'proyects': proyects,  
            'user_name': req.user.username  
        })
    else:
        return redirect('no_access_view')  
    
# SEARCH PROYECT ######################################################################################################
def search_proyect_view(req):
    return render(req, "search_proyect_view.html")

def result_proyect_view(req):
    form = SearchProyectForm(req.GET)

    if form.is_valid():
        user = form.cleaned_data.get('user')  
        name_proyect = form.cleaned_data.get("name_proyect")
        brief_description = form.cleaned_data.get("brief_description")
        key_words = form.cleaned_data.get("key_words")

        proyects = Proyects.objects.all()

        if user:
            proyects = proyects.filter(user__username__icontains=user) 
        if name_proyect:
            proyects = proyects.filter(name_proyect__icontains=name_proyect)
        if brief_description:
            proyects = proyects.filter(brief_description__icontains=brief_description)
        if key_words:
            proyects = proyects.filter(key_words__icontains=key_words)

        return render(req, "result_proyect_view.html", {
            "proyects": proyects,
            "form": form,
        })
    
    return render(req, "search_proyect_view.html", {"form": form})
######################################################################################################################


# ADD PROYECT

def NewProyectForm_view(req):
    user = req.user  

    if req.method == 'POST':
        form_new_proyect = NewProyectForm(req.POST)
        
        if form_new_proyect.is_valid():  
            new_proyect = Proyects(
                user=user,  
                name_proyect=form_new_proyect.cleaned_data["name_proyect"],
                brief_description=form_new_proyect.cleaned_data["brief_description"],
                key_words=form_new_proyect.cleaned_data["key_words"],
            )
            new_proyect.save()  
            return render(req, "proyect_uploaded.html", {})  # Redirecciona tras guardado
    else:
        form_new_proyect = NewProyectForm(initial={'email': user.email})

    return render(req, "NewProyectForm_view.html", {
        "form_new_proyect": form_new_proyect,
        "user_name": user.username  
    })