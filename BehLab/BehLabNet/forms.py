from django import forms
from .models import Proyects


class NewProyectForm(forms.ModelForm):
    email = forms.EmailField(label="Email del usuario") 

    class Meta:
        model = Proyects
        fields = ['name_proyect', 'brief_description', 'key_words']  
        widgets = {
            'brief_description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
        }


class SearchProyectForm(forms.Form):
    user = forms.CharField(max_length=500, required=False, label="Usuario")
    name_proyect = forms.CharField(max_length=500, required=False, label="Nombre del Proyecto")
    brief_description = forms.CharField(max_length=1250, required=False, label="Descripción Breve")
    key_words = forms.CharField(max_length=500, required=False, label="Palabras Clave")