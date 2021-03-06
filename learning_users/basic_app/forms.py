from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from basic_app.models import UserProfileInfo


class UserForm(forms.ModelForm):
    Password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')


class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo 
        fields = ('portfolio','profile_pic') 