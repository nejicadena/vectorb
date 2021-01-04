from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class ModelValid(models.Model):

    user = models.ForeignKey(User, related_name="valid", on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    state_civil = models.CharField(max_length=50)
    n_hijos = models.IntegerField()
    lugar = models.CharField( max_length=50)
    profesion = models.CharField( max_length=50)
    especialidad = models.CharField( max_length=50)
    posgrado = models.CharField( max_length=50)
    time_ex = models.CharField( max_length=50)
    work = models.CharField( max_length=50)
    service = models.CharField( max_length=50)
    sick =models.CharField( max_length=50)
    who = models.CharField( max_length=50)

    def __str__(self):
        return '{}'.format(str(self.user))