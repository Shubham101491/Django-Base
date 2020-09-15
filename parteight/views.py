from django.shortcuts import render,redirect
from parteight.models import Employee
from parteight.forms import EmployeeForm


def crud(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('http://127.0.0.1:8000/parteight/show/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'parteight/crud.html',{'form':form})

def show(request):
    a = Employee.objects.all()
    return render(request,'parteight/show.html',{'emp':a})

def edit(request,id):
    b = Employee.objects.get(id=id)
    return render(request,'parteight/edit.html',{'r':b})

def update(request,id):
    c = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,instance= c)

    if form.is_valid():
        form.save()
        return redirect("http://127.0.0.1:8000/parteight/show/")

    return render(request,'parteight/edit.html',{'r':c})

def delete(request,id):
    d = Employee.objects.get(id=id)
    d.delete()
    return redirect('http://127.0.0.1:8000/parteight/show/')