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
    age = models.IntegerField(null=True,blank=True)
    wechat =models.CharField(max_length=10,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    citizenship = CountryField()

    address_at_duke = models.CharField(max_length=200,null=True,blank=True)
    department_at_duke= models.CharField(max_length=200,null=True,blank=True)
    undergraduate_school = models.CharField(max_length=200,null=True,blank=True)
    company= models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name="RideUser"

class Flight(models.Model):
    flight_number = models.CharField(max_length=256,primary_key=True)
    arrival_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    terminal =models.CharField(max_length=20)
    
    def __str__(self):
        return "Flight %s" % self.flight_number

class NewStudent(RideUser):
    
    flight=models.ForeignKey(Flight)
    luggage_checked_num= models.IntegerField()
    luggage_carryon_num= models.IntegerField()
    backpack_num=models.IntegerField()
    picked=models.BooleanField(default=False)

    class Meta:
        verbose_name="NewStudent"

class Car(models.Model):
    plate_number=models.CharField(max_length=20, primary_key=True)
    capacity= models.IntegerField()
    def __str__(self):
        return "Car %s" % self.plate_number

class Volunteer(RideUser):

    #available_time = models.DurationField()
    car_plate=models.ForeignKey(Car)
    driver_license = models.CharField(max_length=50)
    class Meta:
        verbose_name="Volunteer"

class Pickup(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    newstudent = models.ForeignKey(NewStudent)
    
