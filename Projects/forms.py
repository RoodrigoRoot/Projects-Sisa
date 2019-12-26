from django import forms
from .models import *


class ProjectRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Projects
        fields = ("name_project", "bussines", "folio", "need", "comments")