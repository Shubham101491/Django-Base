from django.shortcuts import render
from django_base import settings

def first(request):
    return render(request,'part2/first.html',{"BASE_URL":settings.BASE_URL})