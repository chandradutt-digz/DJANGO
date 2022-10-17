from statistics import mode
from django.db import models

# Create your models here.
class Enquire(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField()
    mobile = models.IntegerField()
    email = models.EmailField()
    # query = models.TextField()

