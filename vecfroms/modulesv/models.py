from django.db import models 
from django.contrib.auth.models import User

# # Create your models here.
# class Comment(models.Model):
    
#     user = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
#     content1 = models.TextField(max_length=160)
#     timestamp = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return '{}'.format(str(self.user))

# class Comment2(models.Model):
    
#     user = models.ForeignKey(User, related_name="comments2", on_delete=models.CASCADE)
#     content2 = models.TextField(max_length=160)
#     timestamp = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return '{}'.format(str(self.user))

# class Comment3(models.Model):
    
#     user = models.ForeignKey(User, related_name="comments3", on_delete=models.CASCADE)
#     content3 = models.TextField(max_length=160)
#     timestamp = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return '{}'.format(str(self.user))        

