from django import forms
from . import models

class UserData(forms.ModelForm):
    class Meta():
        model = models.userform
        fields='__all__'