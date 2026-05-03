from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Sneaker, Condition
from .forms import CollectingForm

# Function Views
def home(request):
    return render(request, 'main_app/home.html')

def about(request):
    return render(request, 'main_app/about.html')

def sneaker_index(request):
    sneakers = Sneaker.objects.all()
    return render(request, 'main_app/index.html', {'sneakers': sneakers})

def sneaker_detail(request, sneaker_id):
    sneaker = Sneaker.objects.get(id=sneaker_id)
    # Get conditions the sneaker DOESN'T have
    id_list = sneaker.conditions.all().values_list('id')
    conditions_sneaker_doesnt_have = Condition.objects.exclude(id__in=id_list)
    collecting_form = CollectingForm()
    return render(request, 'main_app/detail.html', {
        'sneaker': sneaker,
        'collecting_form': collecting_form,
        'conditions': conditions_sneaker_doesnt_have
    })

# Sneaker CBVs
class SneakerCreate(CreateView):
    model = Sneaker
    fields = ['brand', 'model', 'colorway', 'year']
    template_name = 'main_app/sneaker_form.html'

class SneakerUpdate(UpdateView):
    model = Sneaker
    fields = ['brand', 'model', 'colorway', 'year']
    template_name = 'main_app/sneaker_form.html'

class SneakerDelete(DeleteView):
    model = Sneaker
    success_url = '/sneakers/'
    template_name = 'main_app/sneaker_confirm_delete.html'

# Condition CBVs
class ConditionCreate(CreateView):
    model = Condition
    fields = ['name', 'color']
    template_name = 'main_app/condition_form.html'

class ConditionList(ListView):
    model = Condition
    template_name = 'main_app/condition_list.html'

class ConditionDetail(DetailView):
    model = Condition
    template_name = 'main_app/condition_detail.html'

class ConditionUpdate(UpdateView):
    model = Condition
    fields = ['name', 'color']
    template_name = 'main_app/condition_form.html'

class ConditionDelete(DeleteView):
    model = Condition
    success_url = '/sneakers/'
    template_name = 'main_app/condition_confirm_delete.html'

# Logic for Many-to-Many and ForeignKey
def add_collecting(request, sneaker_id):
    form = CollectingForm(request.POST)
    if form.is_valid():
        new_collecting = form.save(commit=False)
        new_collecting.sneaker_id = sneaker_id
        new_collecting.save()
    return redirect('sneaker-detail', sneaker_id=sneaker_id)

def associate_condition(request, sneaker_id, condition_id):
    Sneaker.objects.get(id=sneaker_id).conditions.add(condition_id)
    return redirect('sneaker-detail', sneaker_id=sneaker_id)

def remove_condition(request, sneaker_id, condition_id):
    Sneaker.objects.get(id=sneaker_id).conditions.remove(condition_id)
    return redirect('sneaker-detail', sneaker_id=sneaker_id)
