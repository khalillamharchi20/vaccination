from django.shortcuts import render
from .models import Question
from django.core.mail import send_mail

# Create your views here.
def index(request):
    a=Question.objects.all().order_by('date')
    question=[]
    reponse= []
    counter=0
    for k in a:
        if k.reponse!="" and counter<9:
            reponse.append(k.reponse)
            question.append(k.question)
            counter=counter+1
    mylist = zip(question, reponse)
    context = {
        'mylist': mylist,
    }
    return render(request, 'index.html',context)
def rdv(request):
    return render(request, 'rdv.html')
def post_question(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    sujet=request.POST.get('subject')
    question=request.POST.get('Message')
    b=Question(name=name,email=email,sujet=sujet,question=question)
    b.save()
    send_mail('vaccination maroc support','nous avons bien recu votre email \n contenue:'+question+'?','corona.vaccination2020@gmail.com',
              [email],False)


    return render(request,'post_question.html')


