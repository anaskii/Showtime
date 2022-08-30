"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('Tsignup',views.Tsignup,name='Tsignup'),
    path('theatersignup',views.theatersignup,name='theatersignup'),
    path('usersignup',views.usersignup,name='usersignup'),
    path('signin',views.signin,name='signin'),
    path('user_login',views.user_login,name='user_login'),
    path('user_logout',views.user_logout,name='user_logout'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('feedback',views.feedback,name='feedback'),
    path('feedback1',views.feedback1,name='feedback1'),
    path('contactus',views.contactus,name='contactus'),
    path('Contact',views.Contact,name='Contact'),
    path('AboutUs',views.AboutUs,name='AboutUs'),
    path('change_password',views.change_password,name='change_password'),
    path('UserProfile', views.UserProfile, name='UserProfile'),
    path('UserEditprofile', views.UserEditprofile, name='UserEditprofile'),
    path('editpofile2',views.editpofile2,name='editpofile2'),
    path('TheaterProfile',views.TheaterProfile,name='TheaterProfile'),
    path('TheaterEditprofile',views.TheaterEditprofile,name='TheaterEditprofile'),
    path('theatereditpofile2',views.theatereditpofile2,name='theatereditpofile2'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
