from django.db import models

# Create your models here.
class individue(models.Model):
    nom=models.CharField(max_length=100,null=False)
    prenom=models.CharField(max_length=100,null=False)
    cin=models.CharField(max_length=100,null=False)
    status=models.BooleanField(null=False,)
class Question(models.Model):
    question=models.CharField(max_length=1000,null=False)
