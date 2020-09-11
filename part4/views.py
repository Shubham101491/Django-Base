from django.shortcuts import render,redirect

from part4.models import Register
from part4.forms import RegisterForm

def forth(request):
    if request.method == "POST":
        form =RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                return redirect('http://127.0.0.1:8000/part3/second/')
            except:
                pass
    else:
        form = RegisterForm()
    return render(request,'part4/modelform.html',{'form':form})