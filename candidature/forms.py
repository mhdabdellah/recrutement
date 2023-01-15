from django import forms
from .models import Candidature

class CandidatureForm(forms.ModelForm):
    class Meta:
        model = Candidature
        fields = ['nom','prenom','email','telephone','cv']
        exclude = ['poste']