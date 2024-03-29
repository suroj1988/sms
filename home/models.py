from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    Type = ((1,'Hod'),(2,'Student'),(3,'staff'))

    user_type = models.CharField(default=1,choices=Type,max_length=200)
    profile_pic = models.ImageField(upload_to='media')


