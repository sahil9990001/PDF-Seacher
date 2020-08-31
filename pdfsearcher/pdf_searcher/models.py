from django.db import models

# Create your models here.


class Post(models.Model):
    sno=models.AutoField(primary_key=True)
    PDF = models.FileField(upload_to='media/')
    