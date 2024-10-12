from django import forms

class csv_upload_form(forms.Form):
    csv_file = forms.FileField(label="Subir archivo CSV")

class InputBoxplot(forms.Form):
    x = forms.CharField(max_length=500, required=True, label="Variable eje x")
    y = forms.CharField(max_length=500, required=True, label="Variable eje y")