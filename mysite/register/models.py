from django.db import models
from django import forms
from django.contrib.auth.models import User #, UserProfile

# Create your models here.

class UserForm(forms.ModelForm):
    class Meta:
        model = User  

"""
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']
"""