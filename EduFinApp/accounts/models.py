
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass
# Create your models here.
from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    role = models.CharField(max_length=20, default='student')

    def __str__(self):
        return self.name