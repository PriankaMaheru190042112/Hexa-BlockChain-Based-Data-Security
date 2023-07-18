from django.db import models
from authentication.models import User

# Create your models here.
class ReadOnlyDocument(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='ReadOnlyDocument/')

    def __str__(self):
        return str(self.file)
