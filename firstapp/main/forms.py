from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    email = forms.EmailField(label="Email")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")



class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password")
    
