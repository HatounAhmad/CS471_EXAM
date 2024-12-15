from django.shortcuts import render
from .models import Games

def home(request):
    return render(request,'videogames/home.html')

def games_list(request):
    Games_list=Games.objects.all()
    return render(request,'videogames/list_games.html',{'Games_list':Games_list})