from django.db import models
from django.contrib.auth.models import User
from countryfield import CountryField
import datetime

# Create your models here.


class RideUser(User):
    GENDER_CHOICES = (
        ('F','Female'),
        ('M','Male'),
        )
    # what is the primary key for User?
    name = models.CharField(max_length=10,null=True,blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES,default='M')
    #age = models.IntegerField(null=True,blank=True)
    wechat =models.CharField(max_length=10,null=True,blank=True)
    phone = models.CharField(max_length=20,null=True,blank=True)
    #citizenship = CountryField()
    # a Boolean determine whehter the user is volunteer or new student
    isVolunteer = models.BooleanField(default = True)

    address_at_duke = models.CharField(max_length=200,null=True,blank=True)
    department_at_duke= models.CharField(max_length=200,null=True,blank=True)
    undergraduate_school = models.CharField(max_length=200,null=True,blank=True)
    company= models.CharField(max_length=200,null=True,blank=True)
    class Meta:
        verbose_name="RideUser"

class Flight(models.Model):
    flight_number = models.CharField(max_length=256,primary_key=True)
    #arrival_time=models.DateTimeField(auto_now=False, auto_now_add=False)
    #terminal =models.CharField(max_length=20)
    
    def __str__(self):
        return self.flight_number

class NewStudent(RideUser):
    #username=models.OneToOneField(User,primary_key=True)
    flight=models.ForeignKey('Flight')
    #a bollean detemine whether a student has been pick up or not
    hasPickup = models.BooleanField(default = False)
    arrival = models.TimeField(null=True)
    arrival_date = models.DateField(default = datetime.date.today)
    models.ImageField(upload_to = 'pic_folder/', default = '')

    #luggage_checked_num= models.IntegerField()
    #luggage_carryon_num= models.IntegerField()
    #backpack_num=models.IntegerField()

    class Meta:
        verbose_name="NewStudent"

class Car(models.Model):
    plate_number=models.CharField(max_length=20, primary_key=True)
    capacity= models.IntegerField(null=True)
    def __str__(self):
        return "Car %s" % self.plate_number

class Volunteer(RideUser):
    #username=models.OneToOneField(User,primary_key=True)
    #available_time = models.DurationField()
    car_plate=models.ForeignKey('Car')
    driver_license = models.CharField(max_length=50)
    class Meta:
        verbose_name="Volunteer"

class Pickup(models.Model):
    volunteer = models.ForeignKey('Volunteer')
    newstudent = models.ForeignKey('NewStudent')
    
