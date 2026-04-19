from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

class Sneaker:
    def __init__(self, brand, model, colorway, releasedate):
        self.brand = brand
        self.model = model
        self.colorway = colorway
        self.resleasedate = releasedate

sneakers = [
    Sneaker('Nike', 'Huarache', 'Scream Green', 1991),
    Sneaker('Air Jordan', 'VII', 'Playoff', 1992),
    Sneaker('Reebok', 'Pump', 'White', 1989),
    Sneaker('Adidas', 'Crazy 8', 'Purple', 1997),
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sneaker_index(request):
    return render(request, 'sneakers/index.html', {'sneakers': sneakers})