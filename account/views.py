from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
# Create your views here.


def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,"signup.html")

def Tsignup(request):
    return render(request,"Tsignup.html")

def signin(request):
    return render(request,"login.html")

def usersignup(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        phono = request.POST.get('phone')
        password = request.POST.get('password')
        location = request.POST.get('location')
        image = request.POST.get('image')


        if User.objects.filter(username=name).count()>0:
            return HttpResponse("username already exist")
        elif User.objects.filter(email=email).count()>0:
            return HttpResponse("email already exist")
        else:

            user=User.objects.create(
                username=name,
                password=make_password(password),
                email=email,is_active=True,
            )
            user.save()
            data=UserSignup.objects.create(user=user,phno=phono,location=location,image=image)
            data.save()
            return redirect('signin')
    else:
        return HttpResponse("Invalid Form")
def theatersignup(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        licno = request.POST.get('licenseno')
        district = request.POST.get('districts')
        location = request.POST.get('location')
        email = request.POST.get('email')
        phno = request.POST.get('phone')
        password = request.POST.get('password')
        theatrename = request.POST.get('theatrename')
        image = request.POSt.get('image')



        if User.objects.filter(username=name).count()>0:
            return HttpResponse("username already exist")
        elif User.objects.filter(email=email).count()>0:
            return HttpResponse("email already exist")
        else:

            user=User.objects.create(
                username=name,
                password=make_password(password),
                email=email,is_active=True,
            )
            user.save()
            theare=TheaterSignup.objects.create(
                user=user,licenseno=licno,phno=phno,district=district,
                location=location,theatre_name=theatrename,image=image,
            )
            theare.save()
            return redirect('signin')
    else:
        return HttpResponse("Invalid Form")



def user_login(request):
    if request.method == "POST":
        name=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=name,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('dashboard')
            else:
                return HttpResponse("Not active")
        else:
            return HttpResponse("Invalid username or password")
    else:
        return render(request,'login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect('index')


def dashboard(request):
    return render(request,"dashboard.html")

def feedback(request):
    return render(request,'feedback.html')

def feedback1(request):

    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        Feed= Feedbackk.objects.create(
            user = request.user,
            feedback = feedback,
        )
        Feed.save()

        return redirect('dashboard')
    else:
        return HttpResponse('Invalid form')

def contactus(request):
    return render(request,'contact.html')


def Contact(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        pho = request.POST.get('pho')
        email = request.POST.get('email')
        address = request.POST.get('address')
        con= ContactUs.objects.create(
            name=name,
            pho=pho,
            email=email,
            address = address,
        )
        con.save()

        return redirect('dashboard')
    else:
        return HttpResponse('Invalid form')


def AboutUs(request):
    return render(request,'aboutus.html')




def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html',{'form': form})


def UserProfile(request):
    user= UserSignup.objects.get(user=request.user)
    return render(request,'User-profile.html',{'user':user})


def UserEditprofile(request):
    user= UserSignup.objects.get(user=request.user)
    print(user.location)
    return render(request,'edit-User-profile.html',{'user':user})



def editpofile2(request):
    if request.method=="POST":
        user = UserSignup.objects.get(user=request.user)
        username=request.POST.get("username")
        image=request.POST.get("image")
        email=request.POST.get("email")
        location=request.POST.get("location")
        phno=request.POST.get("phno")

        user.user.username=username
        user.user.email=email
        user.user.save()

        if image=='' or image==None:
            user.image=user.image
        else:
            user.image=image
        user.location=location
        user.phno=phno
        user.save()

        return redirect('UserProfile')




def TheaterProfile(request):
    theater = TheaterSignup.objects.get(user=request.user)
    return render(request,'Theater-profile.html',{'theater':theater})

def TheaterEditprofile(request):
    theater = TheaterSignup.objects.get(user=request.user)
    return render(request,'edit-theater-profile.html',{'theater':theater})

def theatereditpofile2(request):
    if request.method=="POST":
        theater = TheaterSignup.objects.get(user=request.user)
        username=request.POST.get("username")
        image=request.POST.get("image")
        licenseno=request.POST.get("licenseno")
        district=request.POST.get("district")
        location=request.POST.get("location")
        phno=request.POST.get("phno")

        theater.user.username=username
        theater.user.save()

        if image=='' or image==None:
            theater.image=theater.image
        else:
            theater.image=image
        theater.location=location
        theater.phno=phno
        theater.district = district
        theater.licenseno = licenseno
        theater.save()

        return redirect('TheaterProfile')


# def usermovie(request):








