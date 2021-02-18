from django.forms import ModelForm
from .models import *

class rdvForm(ModelForm):
    class Meta:
        model = pation
        fields = '__all__'