from urllib import request
from django.views.generic import TemplateView, DetailView, CreateView
from django.shortcuts import render

from .models import Jobseeker
from .form import JobseekerForm


class IndexView(TemplateView):
    template_name = 'technologist/index.html'


class H701View(CreateView):
    model = Jobseeker
    form_class = JobseekerForm
    content = Jobseeker.objects.all()
    template_name ='technologist/H701.html'


