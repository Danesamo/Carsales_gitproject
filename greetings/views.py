from django.shortcuts import render
from .models import Equipe
from cars.models import Car

def home(request):
    equipes = Equipe.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    data = {
        'equipes': equipes,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
    }
    return render(request, 'greetings/home.html', data)

def about(request):
    equipes = Equipe.objects.all()
    data = {
        'equipes': equipes,
    }
    return render(request, 'greetings/about.html', data)

def services(request):
    return render(request, 'greetings/services.html')

def contact(request):
    return render(request, 'greetings/contact.html')
