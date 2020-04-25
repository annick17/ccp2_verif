from django.shortcuts import render

# Create your views here.


def base(request) :
    return render (request, 'base/base.html', {})


def accueil(request) :
    return render (request,'base/accueil.html', {})


