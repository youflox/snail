from django.db import models
from django.contrib.auth.models import User

from file_upload.models import File
    
# Create your models here.

class Data(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    userId = models.IntegerField()
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)

    def __str__(self):
        return "user-"+str(self.id)+"__"+str(self.title)
