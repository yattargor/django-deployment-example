from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    #model class to give additional field that User (that I import) not have
    user = models.OneToOneField(User)

    #additional
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    #Possible write this for inheredit from User model
    def __str__(self):
        return self.user.username
