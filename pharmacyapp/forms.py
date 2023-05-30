from django import forms
from .models import depadmin


class depforms(forms.ModelForm):
    class Meta:
        model=depadmin
        fields='__all__'
