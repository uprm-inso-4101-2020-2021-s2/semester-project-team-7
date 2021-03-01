from django.db import models


# Create your models here.
class profiles(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    birth = models.DateField()
    languages = models.CharField(max_length=100)
    description = models.TextField()



