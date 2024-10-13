from django import forms

class csv_upload_form(forms.Form):
    csv_file = forms.FileField(label="Subir archivo CSV")
    def clean_csv_file(self):
        csv_file = self.cleaned_data.get('csv_file')
        if not csv_file.name.endswith('.csv'):
            raise forms.ValidationError('El archivo cargado no es un archivo CSV. Por favor, cargue un archivo con extensión .csv.')
        return csv_file

class InputBoxplot(forms.Form):
    x = forms.CharField(max_length=500, required=True, label="Variable eje x")
    y = forms.CharField(max_length=500, required=True, label="Variable eje y")
    