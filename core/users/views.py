from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import User
from .forms import SignUpForm


def success(request):
	return render(request, 'users/success.html')



class SignUp(CreateView):
    template_name = 'users/sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('users:success')