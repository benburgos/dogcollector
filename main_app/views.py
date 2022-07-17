from django.shortcuts import render
from django.http import HttpResponse
from .models import Dog, dogs

# Create your views here.

def home(request):
    return HttpResponse("<h1>Woof! ฅ^•ﻌ•^ฅ</h1>")


def about(request):
    return render(request, 'about.html')


def dogs_index(request):
    return render(request, 'dogs/index.html', { 'dogs': dogs })
