from django.shortcuts import render
from django_base import settings

def type(request):
    return render(request,'base1/index.html',{"BASE_URL":settings.BASE_URL})