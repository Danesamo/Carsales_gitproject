from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),       # Inclure les URLs de l'application greetings
    path('about', views.about, name='about'),  #about is the method name
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),

]
