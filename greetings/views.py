from django.shortcuts import render

def home(request):
    return render(request, 'greetings/home.html')

def about(request):
    return render(request, 'greetings/about.html')

def services(request):
    return render(request, 'greetings/services.html')

def contact(request):
    return render(request, 'greetings/contact.html')
