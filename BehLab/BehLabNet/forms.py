from django import forms


class NewProyectForm(forms.Form):
    name_proyect = forms.CharField()
    brief_description = forms.CharField(widget=forms.Textarea)

class SearchProyectForm(forms.Form):
    name_proyect = forms.CharField(max_length=51)