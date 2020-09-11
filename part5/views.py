from django.shortcuts import render

def tagging(request):
    return render(request,'part5/tag.html')

def new(request):
    return render(request,'part5/new.html')

def other(request):
    return render(request,'part5/other.html')