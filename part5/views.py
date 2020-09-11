from django.shortcuts import render
from django_base import settings

def fifth(request):
    return render(request,'part5/temp_tagging.html',{"BASE_URL":settings.BASE_URL})

def new(request):
    return render(request,'part5/new.html',{"BASE_URL":settings.BASE_URL})

def other(request):
    return render(request,'part5/other.html',{"BASE_URL":settings.BASE_URL})
