from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from BehLabNet.models import Proyects
from .models import Avatar
from .forms import AvatarForm
import os
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.detail import DetailView
from BehLabNet.forms import NewProyectForm
from django import forms

# Create your views here.

def user_panel_view(req):
    return render(req, "user_panel_view.html", {})

def user_panel_view(req):
    return render(req, "user_panel_view.html", {})

def user_proyects_view(req):
    proyects = Proyects.objects.filter(user=req.user)  
    return render(req, "user_proyects_view.html", {
        'proyects': proyects,  
        'user_name': req.user.username 
    })

# CRUD
class ProyectDelete(DeleteView):
    model = Proyects
    template_name = 'delete_proyects_view.html'
    success_url = '/users/user_proyects_view'
    context_object_name = 'proyect'

class ProyectDetail(DetailView): 
    model = Proyects 
    template_name = 'detail_proyects_view.html'
    context_object_name = 'proyect'

class ProyectUpdate(UpdateView):
    model = Proyects
    form_class = NewProyectForm  # Usa el formulario que definiste
    template_name = 'update_proyects_view.html'
    success_url = '/users/user_proyects_view'
    context_object_name = 'proyect'


# NEW PROYECT (NewProyectForm_view) esta en la app BehLabNet, fue por un cambio de estrategia que hice luego sobre como crear los proyectos


# LOG-IN

def login_view(req):
    form = AuthenticationForm(req, data=req.POST)
    

    if req.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            username = data['username']
            password = data['password']

            user = authenticate(username=username, password=password)
            if user:
                login(req, user)
                return render(req, 'main.html', {'mensaje': f'Bienvenido {username}'})
            else:
                return render(req, 'main.html', {'mensaje': 'Datos incorrectos'})
        else:
            return render(req, 'login_view.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(req, 'login_view.html', {'form': form})
    

@login_required 
def logout_view(req):
    logout(req)
    return render(req, 'main.html', {'mensaje': 'Has cerrado sesión exitosamente'})

# SUSCRIBE

def register_view(req):
    
    if req.method == 'POST':
        form = UserCreationForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data 
            username = data['username'] 
            form.save()
            return render(req, 'main.html', {'mensaje': f'Usuario {username} creado exitosamente'})
        else:
            return render(req, 'register_view.html', {'form': form}) 
    else:
        form = UserCreationForm()
        return render(req, 'register_view.html', {'form': form})
    


# EDIT USER

@login_required  
def edit_user_view(req):
    usuario = req.user  

    if req.method == 'POST':
        form = UserEditForm(req.POST, instance=usuario)  
        if form.is_valid():
            data = form.cleaned_data
            usuario.first_name = data['first_name'] 
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data['password1']) 
            usuario.save()
            return render(req, 'edit_user_view.html', {'mensaje': f'Datos ingresados'})
        else:
            return render(req, 'edit_user_view.html', {'form': form, 'mensaje': 'Ha ocurrido un error'})
    else:
        form = UserEditForm(instance=req.user)  
        return render(req, 'edit_user_view.html', {'form': form})
    

# ADD AVATAR

@login_required
def add_avatar_view(req):
    if req.method == 'POST':
        form = AvatarForm(req.POST, req.FILES)
        if form.is_valid():
            data = form.cleaned_data

            avatar = Avatar.objects.filter(user=req.user).first()
            if avatar:
                # Eliminar la imagen antigua
                if avatar.imagen and os.path.isfile(avatar.imagen.path):
                    os.remove(avatar.imagen.path)
                avatar.imagen = data['imagen']
            else:
                avatar = Avatar(user=req.user, imagen=data['imagen'])  

            avatar.save()
            return render(req, "main.html", {"mensaje": "Avatar actualizado"})
        else:
            return render(req, "add_avatar_view.html", {"form": form})
    else:
        form = AvatarForm()
        return render(req, "add_avatar_view.html", {"form": form})
    