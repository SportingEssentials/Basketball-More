from django.shortcuts import render
from .models import Scent, BasketballEssential, Watch


def home(request):

    return render(request, 'home.html')


def essentials(request):
    basketball_essentials = BasketballEssential.objects.all()




    # Add additional attributes as needed
  # Calculate the number of stars for each basketball essential
    for essential in basketball_essentials:
        num_full_stars = int(essential.stars)
        num_half_stars = round((essential.stars - num_full_stars) * 2)
        essential.num_stars = '★' * num_full_stars + '½' * num_half_stars + '☆' * (5 - num_full_stars - num_half_stars)
    
    context = {
        'basketball_essentials': basketball_essentials,
    
        
    }
    return render(request, 'essentials.html', context)


def cologne(request):
    scents = Scent.objects.all()
    context = {
        'scents':scents
    }
    return render(request, 'cologne.html', context)


def injury(request):
    return render(request, 'injury.html')

def watch(request):
    watches = Watch.objects.all()
    context = {
        'watches':watches
    }
    return render(request, 'watch.html', context)


def gamechanger(request):
    return render(request, 'gamechanger.html')