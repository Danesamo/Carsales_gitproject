from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')   #recuperation de toutes les donnees
    paginator = Paginator(cars, 2)                 #pour la gestion de la pagination dans une page , 3 indique le nombre de voitures(donnees) nous voulons afficher
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)           # ces 3 donnees sont stockees dans 'paged_cars'
    
    #s'assurer de l'unicite des valeurs (mot cle "distinct") pour la requete dans la bd
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    
    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)           #recuperer un objet de la BD

    data = {
        'single_car': single_car,
    }

    return render(request, 'cars/car_detail.html', data)  

def search(request):
    cars = Car.objects.order_by('-created_date')
    
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:         #si le mot cle est dans lurl, alors cest exactement cela qui sera affiche, et sil nest pas vide , on affiche la description de celui ci(descr__icontains)
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:         #si le mot cle est dans lurl, alors cest exactement cela qui sera affiche, et sil nest pas vide , on affiche le modele de celui ci(model__iexact)
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)
    
    if 'city' in request.GET:         #si le mot cle est dans lurl, alors cest exactement cela qui sera affiche, et sil nest pas vide , on affiche le modele de celui ci(model__iexact)
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:         #si le mot cle est dans lurl, alors cest exactement cela qui sera affiche, et sil nest pas vide , on affiche le modele de celui ci(model__iexact)
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)
    
    if 'body_style' in request.GET:         #si le mot cle est dans lurl, alors cest exactement cela qui sera affiche, et sil nest pas vide , on affiche le modele de celui ci(model__iexact)
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)
        
    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission': transmission_search,
    }
    return render(request, 'cars/search.html', data)