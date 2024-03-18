from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    Type = ((1,'Hod'),(2,'Student'),(3,'Teacher'))

    user_type = models.CharField(choices=Type,max_length=200,default=1)
    profile_pic = models.ImageField(upload_to='media')


