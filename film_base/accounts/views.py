from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponse
from django.views.generic.detail import DetailView
from .forms import RegistrationForm
from typing import Any, Dict

from django import http # is not important
from django.shortcuts import redirect, render
from django.urls import reverse

from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.base import View, TemplateView


def register_page(request):

    if request.user.is_authenticated:
        messages.warning(request, "You've aleready been authenticated")
        
        return redirect(reverse('film_list'))

    form = RegistrationForm()

    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for ${user}')

            return redirect(reverse('login'))

    context = {'form': form}
    return render(request, 'accounts/register.html', context)


class ProfileView(LoginRequiredMixin, TemplateView):
    permission_denied_message = "NO! You are not authenticated for this action!"
    login_url = 'login/'
    raise_exception = True
    template_name = 'accounts/profile.html'


