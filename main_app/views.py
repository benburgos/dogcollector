from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog, FavoriteTreat
from .forms import MealForm


def home(request):
    return HttpResponse("<h1>Woof! ฅ^•ﻌ•^ฅ</h1>")


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    treats_dog_doesnt_like = FavoriteTreat.objects.exclude(id__in = dog.treats.all().values_list('id'))
    meal_form = MealForm()
    return render(request, 'dogs/detail.html', {'dog': dog, 'meal_form': meal_form, 'treats': treats_dog_doesnt_like})

def assoc_treat(request, dog_id, treat_id):
    Dog.objects.get(id=dog_id).treats.add(treat_id)
    return redirect('detail', dog_id=dog_id)

def add_meal(request, dog_id):
    form = MealForm(request.POST)
    if form.is_valid():
        new_feeding = form.save(commit=False)
        new_feeding.dog_id = dog_id
        new_feeding.save()
    return redirect('detail', dog_id=dog_id)


class DogCreate(CreateView):
    model = Dog
    fields = '__all__'
    success_url = '/dogs/'


class DogUpdate(UpdateView):
    model = Dog
    fields = ['breed', 'description', 'age']


class DogDelete(DeleteView):
    model = Dog
    success_url = '/dogs/'


class FavoriteTreatList(ListView):
    model = FavoriteTreat


class FavoriteTreatDetail(DetailView):
    model = FavoriteTreat


class FavoriteTreatCreate(CreateView):
    model = FavoriteTreat
    fields = '__all__'


class FavoriteTreatUpdate(UpdateView):
    model = FavoriteTreat
    fields = ['name', 'flavor']


class FavoriteTreatDelete(DeleteView):
    model = FavoriteTreat
    success_url = '/treats/'
