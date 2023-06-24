from django.shortcuts import render
from .models import Scent


def home(request):
    scents = Scent.objects.all()
    context = {
        'scents':scents
    }
    return render(request, 'home.html', context)

