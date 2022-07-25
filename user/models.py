from statistics import mode
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    # username = models.CharField(max_length=10)
    university = models.CharField(max_length=100)
    track = models.CharField(max_length=10)

    # USERNAME_FIELD = 'username'