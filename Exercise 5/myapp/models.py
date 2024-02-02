from django.db import models

# Create your models here.
class userform(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name = models.CharField(max_length=30)
    Email = models.EmailField()
