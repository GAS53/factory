from .models import Jobseeker
from django.forms import ModelForm


class JobseekerForm(ModelForm):

    class Meta:
        model = Jobseeker
        fields = '__all__'