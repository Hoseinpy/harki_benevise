from django import forms
from .models import MAinPageModel


class MainPageForm(forms.ModelForm):
    class Meta:
        model = MAinPageModel
        fields = '__all__'