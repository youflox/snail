from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class File(models.Model):
    file = models.FileField(upload_to="user_uploads/", null=False)
    data_uploaded = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


    def __str__(self):
        return str(self.user_id)+"__"+str(self.file)+"__"+str(self.id)