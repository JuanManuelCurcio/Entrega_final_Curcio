from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .models import Avatar
from .forms import AvatarForm
import os
from django.contrib.auth import logout
from django.shortcuts import redirect

# Create your views here.


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
            data = form.cleaned_data # 1- data son los datos ya validados, de data sacamos
            username = data['username'] # 2- el dato username como username, para 
            form.save()
            return render(req, 'main.html', {'mensaje': f'Usuario {username} creado exitosamente'}) # 3- enviarlo en este mensaje
        else:
            return render(req, 'register_view.html', {'form': form}) 
    else:
        form = UserCreationForm()
        return render(req, 'register_view.html', {'form': form})
    


# EDIT USER

@login_required  # Solo los usuarios logueados pueden acceder a esta vista
def edit_user_view(req):
    usuario = req.user  # El usuario que va a modificar sus datos

    if req.method == 'POST':
        form = UserEditForm(req.POST, instance=usuario)  # Instancia el formulario con los datos del usuario actual aparecen previamente escritos, ANTES UserChangeForm
        if form.is_valid():
            data = form.cleaned_data
            usuario.first_name = data['first_name'] # first_name es el nombre que va a llevar el campo, no se porque lo puso en ingles
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data['password1']) # set_password es un metodo para editar password asi que viene con la encriptacion todo
            usuario.save()
            return render(req, 'edit_user_view.html', {'mensaje': f'Datos ingresados'})
        else:
            return render(req, 'edit_user_view.html', {'form': form, 'mensaje': 'Ha ocurrido un error'})
    else:
        form = UserEditForm(instance=req.user)  # Pasa los datos actuales del usuario al formulario
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
                avatar = Avatar(user=req.user, imagen=data['imagen'])  # Crear nuevo avatar

            avatar.save()
            return render(req, "main.html", {"mensaje": "Avatar actualizado"})
        else:
            return render(req, "add_avatar_view.html", {"form": form})
    else:
        form = AvatarForm()
        return render(req, "add_avatar_view.html", {"form": form})
    