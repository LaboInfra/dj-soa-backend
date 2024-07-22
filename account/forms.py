from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from django.contrib.auth.forms import UserChangeForm as DjangoUserChangeForm
from django import forms

from .models import User


class UserCreationForm(DjangoUserCreationForm):

    class Meta:
        model = User
        fields = ("email",)


class UserChangeForm(DjangoUserChangeForm):

    class Meta:
        model = User
        fields = ("email",)


class UserLogin(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your@email.com'
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'your password'
        })
    )