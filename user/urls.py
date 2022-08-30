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
    path('movie',views.movie,name='movie'),
    path('yearmovies',views.yearmovies,name='yearmovies'),
    path('search_theatre',views.search_theatre,name='search_theatre'),
    path('yearsearchmovies',views.yearsearchmovies,name='yearsearchmovies'),
    path('search_movie',views.search_movie,name='search_movie'),
    path('movie_review/<int:id>',views.movie_review,name='movie_review'),
    path('movie_reviews/<int:id>',views.movie_reviews,name='movie_reviews'),
    path('view_review',views.view_review,name='view_review'),
    path('moviebooking/<int:id>',views.moviebooking,name='moviebooking'),

    path('display_search_movie',views.display_search_movie,name='display_search_movie'),
    path('view_theatre_movie/<int:id>',views.view_theatre_movie,name='view_theatre_movie'),
    path('view_english_movies',views.view_english_movies,name='view_english_movies'),
    path('view_malayalam_movie',views.view_malayalam_movie,name='view_malayalam_movie'),
    path('view_hindi_movie',views.view_hindi_movie,name='view_hindi_movie'),
    path('view_action_movies',views.view_action_movies,name='view_action_movies'),
    path('view_Fantasy_movies',views.view_Fantasy_movies,name='view_Fantasy_movies'),
    path('view_drama_movies',views.view_drama_movies,name='view_drama_movies'),
    path('view_Romantic_movies',views.view_Romantic_movies,name='view_Romantic_movies'),
    path('view_comedy_movies',views.view_comedy_movies,name='view_comedy_movies'),

    path('moviebooking2/<int:id>',views.moviebooking2,name='moviebooking2'),
    path('select_seats',views.select_seats,name='select_seats'),
    path('viewbookedmovies',views.viewbookedmovies,name='viewbookedmovies'),



]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

