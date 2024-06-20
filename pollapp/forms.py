from django import forms
from .models import *
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm

class voterform(forms.ModelForm):
    class Meta:
        model=Voter
        fields="__all__"
        exclude=['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','password1','password2']


class candidateform(forms.ModelForm):
    class Meta:
        model=Candidate
        fields="__all__"
        
class feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields="__all__"