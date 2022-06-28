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
from .forms import LoginForm
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.contrib.auth import logout
from .forms import CustomUserCreationForm, CustomUserChangeForm, LoginForm
from .models import CustomUser
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as log_in

class IndexView(TemplateView):
    template_name = 'authorization/index.html'

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,  username=cd['username'],  password=cd['password'])

        if user is not None:
            if user.is_active:
                log_in(request, user)
               
                return  render(request, 'authorization/index.html', {'form': form})
            else:
                
                return render(request, 'authorization/bad_account.html')
        else:
            
            return render(request, 'authorization/bad_login.html')
    else:
        form = LoginForm()
    return render(request, 'authorization/login.html', {'form': form})





class CustomLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        messages.add_message(self.request, messages.INFO, _("Совершен выход!"))
        return super().dispatch(request, *args, **kwargs)

def logout_view(request):
    logout(request)
    return render(request, 'authorization/index.html')

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

