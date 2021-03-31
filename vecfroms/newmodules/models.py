from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Modelmodule12(models.Model):
    user = models.ForeignKey(User, related_name="moduleUser12", on_delete=models.CASCADE)
    consecuencias = models.CharField(max_length=250)
    refiere = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(str(self.user))