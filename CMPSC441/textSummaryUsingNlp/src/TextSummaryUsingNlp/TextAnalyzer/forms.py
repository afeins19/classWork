from django import forms
from django.core.validators import FileExtensionValidator

class TextInputForm(forms.Form):
    form_name = "Insert the text here"
    text = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}), required=False)
    upload_file = forms.FileField(required=False, validators=[FileExtensionValidator(['pdf'])])

