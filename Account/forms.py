from django.db import models
from django.forms import ModelForm
from .models import SignUp
from django.contrib.auth.hashers import make_password

from django import forms


# class UserForm(ModelForm):
#     class Meta:
#         model=User
#         #fields=__all__
#         fields=['username','password','email']

#     def save(self,commit=True,*args, **kwargs):
#         m=super().save(commit=False)
#         m.password=make_password(self.cleaned_data.get('password'))
#         m.username=self.cleaned_data.get('username').lower()
        
#         if commit:
#             m.save()
#         return m

# class UserDetailsForm(ModelForm):
#     lastname=forms.CharField(required=False)
#     class Meta:
#         model=UserDetails
#         fields=['firstname','lastname','username','email','address']

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password_repeat = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
