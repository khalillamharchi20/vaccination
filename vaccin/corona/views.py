from django.shortcuts import render
from .models import *

# Create your views here.
def welcome(request):
    return render(request,'signin.html')
def prend_un_rendez_vous(request):
    return render(request,'rendez_vous.html')

