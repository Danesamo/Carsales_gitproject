from django.shortcuts import render
from .models import Equipe

def home(request):
    equipes = Equipe.objects.all()
    data = {
        'equipes': equipes,
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
