from django.db import models
from django.forms import ImageField

# Create your models here.

class User(models.Model):
    pic = models.ImageField(upload_to = "static")