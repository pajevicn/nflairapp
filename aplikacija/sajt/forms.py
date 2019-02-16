from django.contrib.auth.models import User
from django.forms import forms
from django.shortcuts import render
from  .models import Prodaja

''' 
class UserForm(forms.ModelForm):
    email=forms.CharField(label="E-mail adresa")
    password=forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email','password']
'''