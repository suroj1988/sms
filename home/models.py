from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime

# Create your models here.
class CustomUser(AbstractUser):
    Type = ((1,'Hod'),(2,'Student'),(3,'staff'))

    user_type = models.CharField(default=1,choices=Type,max_length=200)
    profile_pic = models.ImageField(upload_to='media')

class Course(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
class SessionYear(models.Model):
    sessionyear_start = models.CharField(max_length=200)
    sessionyear_end = models.CharField(max_length=200)

    def __str__(self):
        return self.sessionyear_start + self.sessionyear_end

class Student(models.Model):
    admin = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    course = models.ForeignKey(Course,on_delete=models.CASCADE)
    session = models.ForeignKey(SessionYear,on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin.first_name


