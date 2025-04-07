from django import forms
from .models import DocumentUpload
from .models import Resign

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentUpload
        fields = '__all__'

class ResignationForm(forms.ModelForm):
    class Meta:
        model = Resign
        fields = '__all__'