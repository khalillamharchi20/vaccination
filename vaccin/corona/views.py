from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.core.mail import send_mail


from datetime import datetime, timedelta

from .form import *
from .models import *
# Create your views here.


def user_profile(request):


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
        # recuperer les info de la form
        form_registration = rdvForm(request.POST)
        # si les donnees sont valides
        if form_registration.is_valid():
            # recuperer la valeur donnee par l utilisateur
            cin_code = request.POST.get('cin')
            date_expiration = request.POST.get('date_expiration')
            nom_ville1 = request.POST.get('nom_ville')
            phone1 = request.POST.get('phone')
            email1 = request.POST.get('email')
            registration = pation.objects.filter(cin=cin_code)
            # verifier l existance du pation
            nbregistration = registration.count()
            print(nbregistration)
            if nbregistration > 0:
                centre_viccins =centre_vaccination.objects.filter(nom_ville=nom_ville1)
                centre_viccins_list= []
                for center in centre_viccins:
                    centre = center.id
                    date_vaccin = date_vaccination.objects.filter(nom_centre=centre)
                    test = True
                    if date_vaccin.count() == 0:
                        date_vaccination1=date_vaccination()
                        date_vaccination2 = date_vaccination()
                        date_vaccination1.date_v=(datetime.today()+timedelta(days=2)).strftime('%Y-%m-%d')
                        date_vaccination2.date_v = (datetime.today()+timedelta(days=23)).strftime('%Y-%m-%d')
                        date_vaccination1.nom_centre = center.id
                        date_vaccination2.nom_centre = center.id
                        date_vaccination1.nombre_passion = 1
                        date_vaccination2.nombre_passion = 1
                        registration.update(nom_ville=nom_ville1, Statue='inscrit', email=email1, phone=phone1, nom_centre=center.nom_centre, date_faccination1=date_vaccination1, date_faccination2=date_vaccination2)
                        date_vaccination1.save()
                        date_vaccination2.save()
                        test = False
                        break
                    else:
                        datemax = max(date_vaccin.date_v)
                        centre_viccins_list.append((center.nom_centre, datemax))
                if test == True:
                    # cherchant le centre de la date de vaccination minimal
                    min=0
                    for i in range(1,len(centre_viccins_list)):
                        if centre_viccins_list[i][1]<centre_viccins_list[min][1]:
                            min=i
                    notre_centre=centre_viccins_list[min][0]
                    notre_date=centre_viccins_list[min][1] - timedelta(days=21)
                    datevacc = date_vaccination.objects.filter(date_v=notre_date, nom_centre=notre_centre)
                    if datevacc.nombre_passion < 100:
                        nombre_passion1 = datevacc.nombre_passion +1
                        datevacc.update(nombre_passion=nombre_passion1)
                        datevacc2 = date_vaccination.objects.filter(date_v=notre_date+timedelta(days=21), nom_centre=notre_centre)
                        datevacc2.update(nombre_passion=nombre_passion1)
                        registration.update(nom_ville=nom_ville1, Statue='inscrit', email=email1, phone=phone1,nom_centre=notre_centre, date_faccination1=datevacc.date_v, date_faccination2=datevacc2.date_v)
                    else:
                        while True:
                            notre_date = datevacc.date_v + timedelta(days=1)
                            date_vaccin = date_vaccination.objects.filter(nom_centre=notre_centre, date_v=notre_date)
                            if date_vaccin.count() == 0:
                                datevacc = date_vaccination()
                                datevacc2 = date_vaccination()
                                datevacc.date_v = notre_date
                                datevacc2.date_v = notre_date + timedelta(days=21)
                                datevacc.nom_centre = notre_centre
                                datevacc.nom_centre = notre_centre
                                datevacc.nombre_passion = 1
                                datevacc2.nombre_passion = 1
                                registration.update(nom_ville=nom_ville1, Statue='inscrit', email=email1, phone=phone1,nom_centre=notre_centre, date_faccination1=datevacc.date_v,date_faccination2=datevacc2.date_v)
                                break
                # modifier les
                context = {'registration': registration}
                return redirect('user_profile')

    context = {'form_registration': form_registration, 'form_login': form_login}
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

def render_pdf_view(request):
    template_path = 'corona/pdf.html'
    conext = {'myvar':'this is your template context'}
    #create a django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="certificat de vaccination.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(conext)

    #create a pdf
    pisa_status = pisa.CreatePDF(
        html, dest=response
    )
    # if error then show some funny view
    if pisa_status.err:
        return HttpResponse('we had some errors <pre>' + html + '</pre>')
    return response


