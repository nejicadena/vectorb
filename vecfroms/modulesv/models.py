from django.db import models 
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    
    user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    content = models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(str(self.user))

