from django.db import models
from datetime import datetime

# Create your models here.
class individue(models.Model):
    nom=models.CharField(max_length=100,null=False)
    prenom=models.CharField(max_length=100,null=False)
    cin=models.CharField(max_length=100,null=False)
    status=models.BooleanField(null=False)
class Question(models.Model):
    question=models.CharField(max_length=5000,null=False)
    sujet=models.CharField(max_length=1000,null=True)
    name=models.CharField(max_length=1000,null=True)
    email=models.EmailField(max_length=100,null=False)
    date = models.DateTimeField(default=datetime.now, blank=True)
    reponse=models.CharField(max_length=5000)
