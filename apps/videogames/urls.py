from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('games/',views.games_list,name='games_list'),

]
