from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.hashers import make_password
from account.models import *


# Create your views here.
def addmovies(request):
    print(request.user)
    return render(request,"movies-add.html")

def addmovies2(request):
    if request.method == 'POST':
        moviename= request.POST.get('moviename')
        movieimage = request.FILES.get('movieimage')
        show1 = request.POST.get('show1')
        show2 = request.POST.get('show2')
        show3 = request.POST.get('show3')
        language = request.POST.get('language')
        genre = request.POST.get('genre')
        cast_crew = request.POST.get('cast_crew')
        year = request.POST.get('year')

        theatre_owner=TheaterSignup.objects.get(user=request.user)

        movie=Movies.objects.create(

            user= request.user,
            theater_owner=theatre_owner,
            moviename = moviename,
            movieimage = movieimage,
            show1 = show1,
            show2 = show2,
            show3 = show3,
            language = language,
            genre = genre,
            cast_crew = cast_crew,
            year = year,
            status = True,

        )
        movie.save()
        return redirect('dashboard')
    else:
        return HttpResponse("Invalid Form")

def view_movie(request):
    movies=Movies.objects.filter(user=request.user)
    return render(request,'movie-view.html', {'data':movies})

def update_movie(request,id):
    movie = Movies.objects.get(id=id)
    return render(request,'movie-edit.html',{'movie':movie})

def update_movie2(request,id):
    movie = Movies.objects.get(id=id)
    print(movie.movieimage)
    if request.method=='POST':
        moviename = request.POST.get('moviename')
        movieimage = request.FILES.get('movieimage')
        show1 = request.POST.get('show1')
        show2 = request.POST.get('show2')
        show3 = request.POST.get('show3')
        language = request.POST.get('language')
        genre = request.POST.get('genre')
        cast_crew = request.POST.get('cast_crew')
        year = request.POST.get('year')

        print(movieimage)

        movie.moviename=moviename

        if movieimage == None or movieimage == '':
            movie.movieimage=movie.movieimage
        else:
            movie.movieimage=movieimage
        movie.show1=show1
        movie.show2=show2
        movie.show3=show3
        movie.language=language
        movie.genre=genre
        movie.cast_crew=cast_crew
        movie.year=year

        movie.save()
        return redirect('view_movie')
    else:
        return HttpResponse('Invalid form')

def delete_movie(request,id):
    movie=Movies.objects.get(id=id)
    movie.delete()
    return redirect('view_movie')




def add_rating(request,id):
    movie=Movies.objects.get(id=id)
    print(movie.ratings)
    return render(request,'add_rating.html',{'movie':movie})


def add_rating2(request,id):
    movie = Movies.objects.get(id=id)
    if request.method == 'POST':
        # user=request.method.POST.get('user ')
        # theater_owner=request.POST.get('theater_owner')
        rating=request.POST.get('rating')


        theater_owner=UserSignup.objects.get(user=request.user)

        rate = Rating.objects.create(

            user=request.user,
            user_signup=theater_owner,
            movie=movie,
            rating=rating,

        )
        rate.save()
        ratings_count=Rating.objects.filter(movie=movie).count()
        ratings=Rating.objects.filter(movie=movie)

        sum_rating=0
        for i in ratings:
            sum_rating=int(i.rating)+sum_rating
        print(sum_rating)
        rating_avg=int(sum_rating)/ratings_count
        movie.ratings=rating_avg
        movie.save()


        return redirect('dashboard')
    else:
        return HttpResponse('invalid form')


