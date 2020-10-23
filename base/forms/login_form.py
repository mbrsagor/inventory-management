from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control form-control-lg', 'placeholder': 'Username', 'required': True,
               'autofocus': True}))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control form-control-lg', 'placeholder': 'Password', 'required': True}))
    remember_me = forms.BooleanField(required=False)
