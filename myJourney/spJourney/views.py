from django.shortcuts import render
from .models import LearningJourney, AboutMe

# Create your views here.
def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'index.html', {'journeys': journeys})

def about_me(request):
    profile = AboutMe.objects.first()
    return render(request, 'aboutMe.html', {'profile': profile})
