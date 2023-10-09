from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Consumer(AbstractUser):

    username = models.EmailField(verbose_name='email-Id',unique=True)
    fname = models.CharField(verbose_name='First Name',max_length=30)
    lname = models.CharField(verbose_name='Last Name',max_length=30)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['fname']