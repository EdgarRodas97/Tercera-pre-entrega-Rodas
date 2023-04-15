from django import forms
from .models import EntrenamientosChirho, MaquinariaEquipoChirho


class EntrenamientosFormChirho(forms.ModelForm):
    class Meta:
        model = EntrenamientosChirho
        fields = ['nombrecurso_chirho']


class MaquinariaEquipoFormChirho(forms.ModelForm):
    class Meta:
        model = MaquinariaEquipoChirho
        fields = ['nombre_chirho', 'modelo_chirho']