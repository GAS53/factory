from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django import forms


class CustomUserCreationForm(UserCreationForm):
    field_order =[
        'username',
        'password1',
        'password1',
        'first_name',
        'last_name',
        'email',
        'phone',
        'date_of_birth',
    ]
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_of_birth',
            )
        field_classes = {'username': UsernameField}


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_of_birth',
            )
        field_classes = {"username": UsernameField}

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    

