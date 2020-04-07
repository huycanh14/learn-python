from django.shortcuts import render, get_object_or_404, redirect
from .models import Main
from news.models import News

# Create your views here.


def home(request):
    # sitename = "MySite | Home"
    # site = Main.objects.filter(pk=3)
    site = Main.objects.get(pk=3)
    news = News.objects.all()
    # sitename = site.name + " | Home"

    return render(request, 'front/home.html', {'site': site, 'news': news})


def about(request):
    # sitename = "MySite | About"
    site = Main.objects.get(pk=3)
    return render(request, 'front/about.html', {'site': site})

def panel(request):
    return render(request, 'back/home.html')
