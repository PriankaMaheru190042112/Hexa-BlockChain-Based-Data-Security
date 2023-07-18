from django.db import models
from django.contrib.auth.models import AbstractUser
from authentication.models import User 

class Document(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    key = models.CharField(max_length=200,default='')

    def __str__(self):
        return str(self.file)