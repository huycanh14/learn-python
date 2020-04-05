from django.shortcuts import render, get_object_or_404, redirect
from .models import Main

# Create your views here.


def home(request):
    # sitename = "MySite | Home"
    # site = Main.objects.filter(pk=3)
    site = Main.objects.get(pk=3)
    # sitename = site.name + " | Home"

    return render(request, 'front/home.html', {'site': site})


def about(request):
    # sitename = "MySite | About"
    site = Main.objects.get(pk=3)
    return render(request, 'front/about.html', {'site': site})
