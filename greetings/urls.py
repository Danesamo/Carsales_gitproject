from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
      # Inclure les URLs de l'application greetings
]
