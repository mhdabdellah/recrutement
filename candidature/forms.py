from django import forms
from .models import Candidature

class NewImage(forms.ModelForm):
    class Meta:
        model = Candidature
        fields ='__all__' 
        exclude=['technicien']