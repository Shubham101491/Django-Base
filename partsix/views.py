from django.shortcuts import render

def new(request):
    context_disc = {'text':'hello world','number':100}
    return render(request,'partsix/new.html',context_disc)

def other(request):
    return render(request,'partsix/other.html')