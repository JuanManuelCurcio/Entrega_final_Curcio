from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar


# USER EDIT FORM

class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text = " ", # aparece ayuda al lado del campo
        widget = forms.HiddenInput(), required=False)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contraseña", widget=forms.PasswordInput) # p1 y p2 nos permitirian que la persona cambie su ccontraseña

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')
# validamos que las dos contraseñas sean iguales
    def clean_password2(self): # clean_NOMBREVAR es un metodo! por lo que si la validacion la hago sobre password2 debo llamarla asi. Debajo la manera mas limpia segun chat:
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]

        if password2 != password1:
            raise forms.ValidationError("Contraseñas no son iguales")
        else:
            return password2
        

# AVATAR FORM

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen'] # por alguna razon tiene que ser con una coma al final