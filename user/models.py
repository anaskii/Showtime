from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from movies.models import Movies



#search movie

class Moviereview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    movie=models.ForeignKey(Movies,on_delete=models.CASCADE,null=True,blank=True)
    review=models.CharField(max_length=600,null=True,blank=True)
    def __str__(self):
        return str(self.user.username)



class Seat(models.Model):
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    showtime = models.CharField(max_length=100,null=True, blank=True)
    seats = models.TextField(null=True, blank=True)
    def __str__(self):
        return str(self.date)

class MovieBooking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True, blank=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True, blank=True)
    showtime = models.CharField(max_length=100,null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    seats=models.TextField(null=True, blank=True)
    paid = models.BooleanField(null=True, blank=True,default=False)

    def __str__(self):
        return str(self.user.username)








