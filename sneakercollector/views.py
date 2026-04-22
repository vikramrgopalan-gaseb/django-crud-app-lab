from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Sneaker
# Create your views here.



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sneaker_index(request):
    return render(request, 'sneakers/index.html', {'sneakers': sneakers})

def sneaker_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    return render(request, 'sneakers/detail.html', {'sneaker': sneaker})

class SneakerCreate(CreateView):
    model = Sneaker
    fields = '__all__'
    # success_url = '/sneakers/'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['brand', 'model', 'colorway', 'releasedate']

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'