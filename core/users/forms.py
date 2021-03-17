from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm, UsernameField, AuthenticationForm
from django.utils.translation import gettext, gettext_lazy as _
from django import forms

from .models import User


class SignUpForm(UserCreationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                           'placeholder': 'Create a username'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                           'placeholder': 'Create a username'}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mt-2',
                                          'placeholder': 'Create a password'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control mt-2',
                                          'placeholder': 'Confirm the password'}),
        strip=False,
        help_text=("Enter the same password as before, for verification."),
    )

    class Meta:
        model = User
        fields = ('username', 'email',)


class SignInForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True, 'class': 'form-control mt-2',
                                                           'placeholder': 'Your username'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class': 'form-control mt-2',
                                          'placeholder': 'Your password'}),
    )