from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    return render(request,'index.html')
def rdv(request):
    return render(request,'rdv.html')

