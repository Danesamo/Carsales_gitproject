from django.shortcuts import render
from .models import Equipe
from cars.models import Car

def home(request):
    equipes = Equipe.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')
    #s'assurer de l'unicite des valeurs (mot cle "distinct") pour la requete dans la bd
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    
    data = {
        'equipes': equipes,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
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
