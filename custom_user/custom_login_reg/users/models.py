from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=30,unique=True)
    date_of_birth = models.DateField()
    height = models.FloatField()

    REQUIRED_FIELDS = ['email', 'height']

    def __str__(self):
        return self.email