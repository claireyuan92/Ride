from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class RideUser(User):

    GENDER_CHOICES = (
        ('F','Female'),
        ('M','Male'),
        )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    age = 
    
    

class Volunteer(RideUser):


class NewStudent(RideUser):

