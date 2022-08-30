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
    path('addmovies',views.addmovies,name='addmovies'),
    path('addmovies2',views.addmovies2,name='addmovies2'),
    path('view_movie',views.view_movie,name='view_movie'),
    path('update_movie/<int:id>',views.update_movie,name='update_movie'),
    path('delete_movie/<int:id>',views.delete_movie,name='delete_movie'),
    path('update_movie2/<int:id>',views.update_movie2,name='update_movie2'),
    path('add_rating/<int:id>',views.add_rating,name='add_rating'),
    path('add_rating2/<int:id>',views.add_rating2,name='add_rating2'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


