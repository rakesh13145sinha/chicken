from django.db import models


# Create your models here.
class Identification(models.Model):
    user_name=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=20)