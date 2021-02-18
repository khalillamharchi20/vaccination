from django.db import models
from datetime import datetime

# Create your models here.



class ville(models.Model):
    nom_ville = models.CharField(max_length=200, primary_key=True)
    def __str__(self):
        return self.nom_ville



class centre_vaccination(models.Model):
    nom_centre = models.CharField(max_length=300)
    nom_ville = models.ForeignKey(ville, max_length=100, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return self.nom_centre


class date_vaccination(models.Model):
    date_v = models.DateTimeField(null=True, blank=True)
    nombre_passion = models.IntegerField(null=True, blank=True)
    nom_centre = models.ForeignKey(centre_vaccination, max_length=300, null=True, blank=True, on_delete=models.SET_NULL)



class pation(models.Model):
    STATUS = (
        ('non_inscrit', 'non_inscrit'),
        ('inscrit', 'inscrit'),
        ('vacciné', 'vacciné')
    )
    FullName_Pation = models.CharField(max_length=300)
    cin = models.CharField(max_length=20)
    date_expiration = models.DateTimeField()
    nom_ville = models.ForeignKey(ville, max_length=100, null=True, blank=True, on_delete=models.SET_NULL)
    email = models.CharField(max_length=300, null=True, blank=True)
    phone = models.CharField(max_length=20, null=True, blank=True)
    Statue = models.CharField(max_length=200 , choices=STATUS)
    nom_centre = models.ForeignKey(centre_vaccination , max_length=300, null=True, blank=True, on_delete=models.SET_NULL)
    date_faccination1 = models.DateTimeField(null=True, blank=True)
    date_faccination2 = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.FullName_Pation


class Question(models.Model):
    question = models.CharField(max_length=5000,null=False)
    sujet = models.CharField(max_length=1000,null=True)
    name = models.CharField(max_length=1000,null=True)
    email = models.EmailField(max_length=100,null=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    reponse = models.CharField(max_length=5000)
    status=models.BooleanField()

