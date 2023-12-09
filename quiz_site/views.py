from django.shortcuts import render
from .models import *


# Create your views here.
def home(request):
    context = {
        'risks': Risk.objects.all(),
        'packages': Package.objects.all()
    }
    return render(request, 'quiz_site/home.html', context)

def about(request):
    return render(request, 'quiz_site/about.html')

def how_it_works(request):
    return render(request, 'quiz_site/how_it_works.html')


