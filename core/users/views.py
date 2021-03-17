from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetView, \
    PasswordResetConfirmView, PasswordResetCompleteView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import *


def success(request):
    return render(request, 'users/success.html')


class SignUp(CreateView):
    template_name = 'users/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:success')


class SignIn(LoginView):
    template_name = 'users/sign_in.html'
    form_class = SignInForm


class SignOut(LogoutView):
    template_name = 'users/sign_in.html'


class PasswordReset(PasswordResetView):
    template_name = 'users/password_reset.html'
    email_template_name = 'users/send_email.html'
    # form_class = PasswordResetForm
    success_url = reverse_lazy('users:password_done')


class PasswordResetDone(PasswordResetDoneView):
    template_name = 'users/password_done.html'


class PasswordResetConfirm(PasswordResetConfirmView):
    template_name = 'users/password_confirm.html'
    success_url = reverse_lazy('users:password_complete')


class PasswordResetComplete(PasswordResetCompleteView):
    template_name = 'users/password_complete.html'
