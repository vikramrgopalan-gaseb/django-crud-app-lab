from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Sneaker, Condition
from .forms import CollectingForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def sneaker_index(request):
    sneaker = Sneaker.objects.all()
    return render(request, 'sneakers/index.html', {'sneakes': sneakers})

def sneaker_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    condition_sneaker_doesnt_have = Condition.objects.exclude(id__in = sneaker.condition.all().values_list('id'))
    collecting_form = CollectingForm()
    return render(request, 'sneakers/detail.html', {'sneakers': sneaker, 'collecting_form': collecting_form, 'condition': condition_sneaker_doesnt_have})

class SneakerCreate(CreateView):
    model = Sneaker
    fields = ['brand', 'model', 'colorway', 'year']
    # success_url = '/cats/'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['brand', 'model', 'colorway', 'year']

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'

def add_collecting(request, sneaker_id):
    form = CollectingForm(request.POST)
    if form.is_valid():
        new_collecting = form.save(commit=False)
        new_collecting.sneaker_id = sneaker_id
        new_collecting.save()
    return redirect('sneaker-detail', sneaker_id=sneaker_id)

class ConditionCreate(CreateView):
    model = Condition
    fields = ['DS', 'NDS', 'W']

class ConditionList(ListView):
    model = Condition

class ConditionDetail(DetailView):
    model = Condition

class ConditionUpdate(UpdateView):
    model = Condition
    fields = ['DS', 'NDS', 'W']

class ConditionDelete(DeleteView):
    model = Condition
    success_url = '/sneakers/'

def associate_condition(request, sneaker_id, condition_id):
    Sneaker.objects.get(id=sneaker_id).condition.add(condition_id)
    return redirect('sneaker-detail', sneaker_id=sneaker_id)

def remove_condition(request, sneaker_id, condition_id):
    Sneaker.objects.get(id=sneaker_id).condition.remove(condition_id)
    return redirect('sneaker-detail', sneaker_id=sneaker_id)