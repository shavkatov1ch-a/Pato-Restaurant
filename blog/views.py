from django.shortcuts import render
from .models import *


def home(request):
    posts = Home.objects.all()
    context = {'posts': posts}
    return render(request, 'index.html', context)


def pato(request):
    arts = Pato.objects.all()
    context = {'arts': arts}
    return render(request, 'index.html', context)

def menu(request):
    pens = Menu.objects.all()
    context = {'pens': pens}
    return render(request, 'index.html', context)

