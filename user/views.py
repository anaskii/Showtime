from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.hashers import make_password
from movies.models import *

# Create your views here.
from account.models import *



def movie(request):
    return render(request,'usermovie-view.html')

def search_theatre(request):
    if request.method=="POST":
        district=request.POST.get("districts")

        theatre=TheaterSignup.objects.filter(district__icontains=district)
        print(theatre)
        return render(request,'usermovie-view.html',{'theatre':theatre})
    else:
        return HttpResponse("Invalid Form")

def view_theatre_movie(request,id):
    theatre=TheaterSignup.objects.get(id=id)
    # print(theatre)
    movies=Movies.objects.filter(theater_owner=theatre)
    print(movies)
    return render(request,'view_theatre_movie.html',{'movies':movies})

def yearmovies(request):
    return render(request,'yearmovie-view.html')

def yearsearchmovies(request):
    if request.method=="POST":
        year=request.POST.get("year")

        theatres=Movies.objects.filter(year=year)
        print(theatres)
        return render(request,'yearsearch-movie-view.html',{'movie':theatres})
    else:
        return HttpResponse("Invalid Form")

def search_movie(request):
    return render(request,'search-movie.html')

def display_search_movie(request):
    if request.method == "POST":
        theater_owner=request.POST.get('theater_owner')
        moviename = request.POST.get('moviename')
        theatre=Movies.objects.filter(theater_owner__theatre_name__icontains=theater_owner)
        print(theatre)
        display=Movies.objects.filter(moviename__icontains=moviename,theater_owner__theatre_name__icontains=theater_owner)
        print(display)
        return render(request,'search-movie.html',{'display':display})
    else:
        return HttpResponse('invalid form')

    #language

def view_english_movies(request):
    movie=Movies.objects.filter(language__icontains="English") | Movies.objects.filter(language__icontains="english")
    print(movie)
    return render(request,'view_english_movie.html',{'movie':movie})

def view_malayalam_movie(request):
    movie=Movies.objects.filter(language__icontains="Malayalm") | Movies.objects.filter(language__icontains="malayalam")
    print(movie)
    return render(request, 'view_malayalam_movie.html', {'movie': movie})


def view_hindi_movie(request):
    hindi_movie=Movies.objects.filter(language__icontains="Hindi") | Movies.objects.filter(language__icontains="hindi")
    print(hindi_movie)
    return render(request, 'view_hindi_movie.html', {'movie': hindi_movie})

#gener
def view_action_movies(request):
    action_movie=Movies.objects.filter(genre__icontains="Action") | Movies.objects.filter(genre__icontains="action")
    print(action_movie)
    return render(request, 'view_action_movies.html', {'movie': action_movie})

def view_Fantasy_movies(request):
    Fantasy_movie=Movies.objects.filter(genre__icontains="Fantasy") | Movies.objects.filter(genre__icontains="fantasy")
    print(Fantasy_movie)
    return render(request, 'view_Fantasy_movies.html', {'movie': Fantasy_movie})

def view_drama_movies(request):
    drama_movie=Movies.objects.filter(genre__icontains="Drama") | Movies.objects.filter(genre__icontains="drama")
    print(drama_movie)
    return render(request, 'view_drama_movies.html', {'movie':  drama_movie})

def view_Romantic_movies(request):
    Romantic_movie=Movies.objects.filter(genre__icontains="Romance") | Movies.objects.filter(genre__icontains="romance")
    print(Romantic_movie)
    return render(request, 'view_Romantic_movies.html', {'movie':Romantic_movie})

def view_comedy_movies(request):
    comedy_movie=Movies.objects.filter(genre__icontains="Comedy") | Movies.objects.filter(genre__icontains="comedy")
    print(comedy_movie)
    return render(request, 'view_action_movies.html', {'movie': comedy_movie})


def movie_review(request,id):
    movie=Movies.objects.get(id=id)
    return render(request,'movie-review.html',{'movie':movie})

def movie_reviews(request,id):
    movie = Movies.objects.get(id=id)
    if request.method == 'POST':
        review= request.POST.get('review')
        rev= Moviereview.objects.create(
            user = request.user,
            movie=movie,
            review = review,
        )
        rev.save()

        return redirect('dashboard')
    else:
        return HttpResponse('Invalid form')

def view_review(request):
    view =Moviereview.objects.all()
    print(view)
    return render(request,'view-review.html',{'view':view})


def moviebooking(request,id):
    book=Movies.objects.get(id=id)
    print(book)
    return render(request,'movie-booking.html',{'book':book})


import simplejson as json

def moviebooking2(request,id):
    movie=Movies.objects.get(id=id)
    request.session['movie_id'] = movie.id
    if request.method=='POST':
        show=request.POST.get("show")
        date=request.POST.get("date")

        request.session['show'] = show
        request.session['date'] = date


        seats_available_count=Seat.objects.filter(movie=movie,showtime=show,date=date).count()
        print(seats_available_count)
        if seats_available_count == 1:
            seats_available=Seat.objects.get(movie=movie, showtime=show, date=date)
            print(seats_available)
            request.session['seats_available'] = seats_available.id
            return redirect('select_seats')
        else:
            seats_create=Seat.objects.create(
                movie=movie,
                date=date,
                showtime=show,
                seats=[],
            )
            request.session['seats_available'] = seats_create.id
            return redirect('select_seats')


def select_seats(request):
    seats_available_id = request.session['seats_available']
    seats_available = Seat.objects.get(id=seats_available_id)
    jsonDec = json.decoder.JSONDecoder()
    booked_seat_list2 = jsonDec.decode(seats_available.seats)
    print(booked_seat_list2)

    if request.method=="POST":
        seats=request.POST.getlist("seats[]")

        movie_id=request.session['movie_id']
        movie=Movies.objects.get(id=movie_id)
        print(movie)
        show=request.session['show']
        print(show)
        date=request.session['date']
        print(date)
        seats_available_id=request.session['seats_available']
        seats_available=Seat.objects.get(id=seats_available_id)
        print(seats_available)

        print(seats)

        seat_list=[]

        for i in seats:
            seat_list.append(i)

        seat_length=len(seat_list)
        request.session['seat_length']=seat_length
        jsonDec = json.decoder.JSONDecoder()
        booked_seat_list = jsonDec.decode(seats_available.seats)
        booked_seat_list=booked_seat_list+seat_list
        request.session['booked_seats']=seat_list

        booking=MovieBooking.objects.create(
            user=request.user,
            movie=movie,showtime=show,
            date=date,seats=json.dumps(seat_list),

        )
        request.session['booking_id']=booking.id
        # print(booking.id)
        print("hi")

        # seats_available.seats=json.dumps(booked_seat_list)
        # seats_available.save()
        return redirect('Payment')

    return render(request,'select-seats.html',{'seats_available':seats_available,'booked_seat_list2':booked_seat_list2})



def viewbookedmovies(request):
    booked = MovieBooking.objects.filter(user=request.user)
    return render(request,'viewbooked-movies.html',{'booked':booked})












