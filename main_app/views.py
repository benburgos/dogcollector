from ast import Delete
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Dog, FavoriteTreat


def home(request):
    return HttpResponse("<h1>Woof! ฅ^•ﻌ•^ฅ</h1>")


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    return render(request, 'dogs/detail.html', {'dog': dog})


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
