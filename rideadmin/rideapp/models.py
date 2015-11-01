from django.db import models
from django.contrib.auth.models import User
from countryfield import CountryField
# Create your models here.


class RideUser(User):
    GENDER_CHOICES = (
        ('F','Female'),
        ('M','Male'),
        )
    # what is the primary key for User?
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    age = models.IntegerField(max_length=2)
    wechat =models.CharField(max_length=10)
    phone = models.CharField(max_length=20)
    citizenship = CountryField()

    address_at_duke = models.CharField(max_length=200)
    department_at_duke= models.CharField(max_length=200)
    undergraduate_school = models.CharField(max_length=200)
    company= models.CharField(max_length=200)
"""

class Flight(models.Model):
    plate_number = models.CharField(max_length=256,primary_key=True)
    capacity = models.IntegerField()

class NewStudent(RideUser):
    flight=models.ForeignKey(Flight)
    luggage_checked_num= models.IntegerField()
    luggage_carryon_num= models.IntegerField()
    backpack_num=models.IntegerField()
    
    
class Volunteer(RideUser):
    available_time = models.DurationField()
    

"""
