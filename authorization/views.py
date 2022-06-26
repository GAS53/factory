from django.views.generic import TemplateView, CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class IndexView(TemplateView):
    template_name = 'authorization/index.html'


class CustomLoginView(LoginView):
    template_name = 'authorization/login.html'
    success_url = 'authorization/index.html'

    def form_valid(self, form):
        res = super().form_valid(form)
        name = self.request.user.get_username()
        messages.add_message(self.request, messages.INFO, mark_safe(_(f'совершон вход {name}')))
        return res

    def form_invalid(self, form):
        res = super().form_invalid(form)
        messages.add_message(self.request, messages.WARNING, mark_safe(_(f'неудачная попытка входа')))
        return res


class CustomLogoutView(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, _("Совершен выход!"))
        return super().dispatch(request, *args, **kwargs)


class ProfileEditView(UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm

    def test_func(self):
        return True if self.request.user.pk == self.kwargs.get("pk") else False
    
    def get_success_url(self):
        return reverse_lazy("authorization:edit_profile", args=[self.request.user.pk])



class RegisterView(CreateView):
    model = get_user_model()
    template_name = 'authorization/register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('authorization:index')

