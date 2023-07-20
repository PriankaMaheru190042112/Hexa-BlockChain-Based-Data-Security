from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_data_owner = models.BooleanField(default=True)
    is_regulators = models.BooleanField(default=False)
    is_analyst = models.BooleanField(default=False)
    institution = models.CharField(max_length=200,default='')