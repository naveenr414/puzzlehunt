from django import forms
from .models import Team

class LoginForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label='password')

    class Meta:
        model = Team
        widgets = {
            'password': forms.PasswordInput(),
        }

class RegisterForm(forms.Form):
    username = forms.CharField(label='Username:', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput, label='Password:')
    confirmPassword = forms.CharField(widget=forms.PasswordInput,label='Confirm Password:')
    teamName = forms.CharField(label='Team Name', max_length=100)

    class Meta:
        model = Team
        widgets = {
            'password': forms.PasswordInput(),
            'confirmPassword': forms.PasswordInput(),
        }


