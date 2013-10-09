from django.db import models

class Festival(models.Model):
    name = models.CharField(max_length=512)
    country = models.CharField(max_length=128)
    date_start = models.DateTimeField()
