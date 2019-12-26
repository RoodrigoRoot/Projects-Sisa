from django import forms
from .models import *

class CustomerRegisterForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ("name_bussines", "representative", "phone", "email")


class CustomerUpdateForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ("name_bussines", "representative", "phone", "email")