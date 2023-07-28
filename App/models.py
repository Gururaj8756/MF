
from django.db import models

# Create your models here.

from django.db import models

class PersonCount(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

