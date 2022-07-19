from distutils.log import error
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Dog, FavoriteTreat, Photo
from .forms import MealForm
import boto3
import uuid

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'dogcollector-bb-88'


def home(request):
    return HttpResponse("<h1>Woof! ฅ^•ﻌ•^ฅ</h1>")


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/index.html', {'dogs': dogs})


def dogs_detail(request, dog_id):
    dog = Dog.objects.get(id=dog_id)
    treats_dog_doesnt_like = FavoriteTreat.objects.exclude(
        id__in=dog.treats.all().values_list('id'))
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


def add_photo(request, dog_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, dog_id=dog_id)
            photo.save()
        except:
            print('An error occurred while uploading the image!')
    return redirect('detail', dog_id=dog_id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again!'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


class DogCreate(CreateView):
    model = Dog
    fields = ['name', 'breed', 'description', 'age']
    success_url = '/dogs/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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
