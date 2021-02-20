from django.forms import ModelForm
from django import forms
from .models import *

class rdvForm(ModelForm):
    class Meta:
        model = pation
        fields = ('cin', 'date_expiration', 'nom_ville', 'phone', 'email')
        widgets = {
            'cin': forms.TextInput(attrs={'class':'form-control', 'type':'text', 'name':'cin', 'id':'cin', 'placeholder':'A00000', 'data-rule':'minlen:4'}),
            'date_expiration': forms.TextInput(attrs={'class':'form-control', 'type':'date', 'name':'exp', 'id':'exp', 'min':'31-1-2021'}),
            'nom_ville': forms.Select(attrs={'class': 'form-control', 'type':'text', 'name':'ville', 'id':'ville'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'type':'tel', 'id':'tel', 'placeholder':'0600000000'}),
            'email': forms.TextInput(attrs={'class': 'form-control', 'name':'email', 'id':'email', 'placeholder':'exemple@email.com', 'data-rule':'email' }),


        }

class loginForm(ModelForm):
    class Meta:
        model = pation
        fields = ('cin', 'date_expiration')
        widgets = {
            'cin' : forms.TextInput(attrs={'class':'form-control', 'type':'text', 'name':'cin', 'id':'cin', 'placeholder':'A00000', 'data-rule':'minlen:4'}),
            'date_expiration': forms.TextInput(attrs={'class': 'form-control', 'type': 'date', 'name': 'exp', 'id': 'exp', 'min': '31-1-2021'}),
        }