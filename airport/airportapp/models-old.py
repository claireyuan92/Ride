from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class UserProfile(models.Model):
	
    user = models.OneToOneField(User)
    
    
    def _str_(self):
    	return self.user.username
    