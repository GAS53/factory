from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    field_order =[
        'login',
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
            'login',
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_of_birth',
            )
        field_classes = {'login': UsernameField}


class CustomUserChangeForm(ModelForm):
    class Meta:
        model = get_user_model()
        fields = (
            'login',
            'first_name',
            'last_name',
            'email',
            'phone',
            'date_of_birth',
            )
        field_classes = {"login": UsernameField}