from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class UserSignup(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    location=models.CharField(max_length=300,null=True,blank=True)
    phno = models.IntegerField(null=True,blank=True)
    image = models.ImageField(upload_to='user_image',null=True,blank=True)
    def __str__(self):
        return str(self.user.username)

class TheaterSignup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    licenseno=models.CharField(max_length=50,null=True,blank=True)
    phno = models.IntegerField(null=True,blank=True)
    district = models.CharField(max_length=100, null=True, blank=True)
    location = models.CharField(max_length=300, null=True, blank=True)
    theatre_name=models.CharField(max_length=300,null=True,blank=True)
    image=models.ImageField(upload_to='theatre_image',null=True,blank=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return str(self.user.username)

class Feedbackk(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback=models.CharField(max_length=600,null=True,blank=True)
    def __str__(self):
        return str(self.user.username)


class ContactUs(models.Model):
    name= models.CharField(max_length=100,null=True,blank=True)
    pho = models.IntegerField(null=True,blank=True)
    email =models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=300,null=True,blank=True)
    message = models.CharField(max_length=300,null=True,blank=True)






