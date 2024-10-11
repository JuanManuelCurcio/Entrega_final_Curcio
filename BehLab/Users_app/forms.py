from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar


# USER EDIT FORM

class UserEditForm(UserChangeForm):
    password = forms.CharField(
        help_text = " ", 
        widget = forms.HiddenInput(), required=False)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'last_name','email')
    def clean_password2(self):
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
        fields = ['imagen']