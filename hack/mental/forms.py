from django import forms
from mental.models import cred_model

class cred_form(forms.ModelForm):
    class Meta:
        model=cred_model
        fields="__all__"