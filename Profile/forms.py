from django import forms
from django.contrib.auth.models import User
from .models import *

class ProfileRegisterForm(forms.ModelForm):
    
    class Meta:
        model = Profile
        fields = ("area",)
        

class UserRegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'id':'username',
                                    'placeholder':'Username'
                                })) 

    email = forms.EmailField(required=True,
                                    widget=forms.EmailInput(attrs={
                                    'id':'email',
                                    'placeholder':'email@email.com'
                                }))

    password = forms.CharField(required=True,
                                    widget=forms.PasswordInput(attrs={
                                    'id':'password',
                                    'placeholder':'password'
                                }))


    password2 = forms.CharField(label='Repeat your password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                }))
    
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username Exists")
            
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Exists")
    
    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'The password is not same')
    
    def save(self):
        return User.objects.create_user(
                                 self.cleaned_data.get('username'),
                                 self.cleaned_data.get('email'),
                                 self.cleaned_data.get('password'),
                                 is_active=True)