from django.shortcuts import render
from .models import Question
from django.core.mail import send_mail
from .form import *
# Create your views here.


def pation(request):


    return render(request, 'corona/user.html')




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
    list1=[]
    list2=[]
    list3=[]
    list4=[]


    for k in range (0,len(reponse)):
        list1.append("collapse")
        list3.append("collapsed")
    for k in range(1,len(reponse)+1):
        list2.append("faq"+str(k))
        list4.append("#faq"+str(k))
    mylist = zip(question, reponse,list1,list2,list3,list4)


    context = {
        'mylist': mylist
    }
    b=Question.objects.all()
    for k in b:
        if k.reponse!="" and k.status==False:
            send_mail('vaccination maroc support', k.reponse,
                      'corona.vaccination2020@gmail.com',
                      [k.email], False)



    return render(request, 'corona/index.html',context)

def rdv(request):
    form_registration = rdvForm()
    form_login = loginForm()
    if request.method == 'POST':

        form_registration = rdvForm(request.POST)
        if form_registration.is_valid():
            form_registration.save()

    context = {'form_registration': form_registration, 'form_login':form_login }
    return render(request, 'corona/rdv.html', context)

def post_question(request):
    name=request.POST.get('name')
    email=request.POST.get('email')
    sujet=request.POST.get('subject')
    question=request.POST.get('Message')
    b=Question(name=name,email=email,sujet=sujet,question=question,status=False)
    b.save()
    send_mail('vaccination maroc support','nous avons bien recu votre email \n contenue:'+question+'?','corona.vaccination2020@gmail.com',
              [email],False)

    return render(request,'corona/post_question.html')

def map(request):
    return render(request, 'corona/map.html')


def blog(request):
    return render(request,'corona/blog.html')



