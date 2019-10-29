from django.db import models

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=300)
    time = models.TimeField(auto_now=True)
    date = models.DateField(auto_now=True)