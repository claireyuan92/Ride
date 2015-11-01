from django.db import models
from django.contrib.auth.models import User
from country.py import CountryField
# Create your models here.

class RideUser(User):

    GENDER_CHOICES = (
        ('F','Female'),
        ('M','Male'),
        )
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    age = models.IntegerField()
    wechat =models.CharField()
    phone = models.CharField()
    residence = model.CharField()
    citizenship = CountryField()
    department_at_duke= models.CharField()
    undergraduate_school = models.CharField()
    company= models.CharField()
    
class Volunteer(RideUser):
    flight
    luggage_checked_num=
    luggage_carryon-num=
    backpack_num=

class NewStudent(RideUser):

