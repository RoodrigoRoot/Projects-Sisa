from django import forms
from .models import *

class CustomerRegisterForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = "__all__"