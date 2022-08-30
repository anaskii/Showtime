from django.db import models
from django.contrib.auth.models import User
from account.models import *
# Create your models here.


class Movies(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    theater_owner = models.ForeignKey(TheaterSignup,on_delete=models.CASCADE,null=True,blank=True)
    moviename = models.CharField(max_length=200,null=True,blank=True)
    movieimage = models.ImageField(upload_to='movieimage',null=True,blank=True)
    show1 = models.CharField(max_length=20,null=True,blank=True)
    show2 = models.CharField(max_length=20,null=True,blank=True)
    show3 = models.CharField(max_length=20,null=True,blank=True)
    language = models.CharField(max_length=20,null=True,blank=True)
    genre = models.CharField(max_length=100,null=True,blank=True)
    cast_crew = models.CharField(max_length=200,null=True,blank=True)
    status = models.BooleanField(default=False)
    year = models.CharField(max_length=20,null=True,blank=True)
    ratings = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return str(self.user.username)



class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    user_signup = models.ForeignKey(UserSignup, on_delete=models.CASCADE, null=True, blank=True)
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE,null=True,blank=True)
    rating=models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.user.username)



