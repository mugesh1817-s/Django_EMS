from django import forms
from .models import DocumentUpload
from .models import Resign
from.models import Career

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = DocumentUpload
        fields = '__all__'

class ResignationForm(forms.ModelForm):
    class Meta:
        model = Resign
        fields = '__all__'

class CareerApplicationForm(forms.ModelForm):
    class Meta:
        model = Career
        fields = '__all__'
        widgets = {
            'job_role': forms.TextInput(attrs={'readonly': 'readonly'}),  # Filled from card click
        }