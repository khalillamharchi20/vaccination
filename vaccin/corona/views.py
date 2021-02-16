from django.shortcuts import render
from .models import *

# Create your views here.
def signin(request):
    a=individue.objects.all()
    temoin=0
    for i in a:
        if i.nom=="lamharchi" and i.prenom=="khalil":
            temoin=1
    print(temoin)

    return render(request,'signin.html')
