from django import forms

class csv_upload_form(forms.Form):
    csv_file = forms.FileField(label="Subir archivo CSV")