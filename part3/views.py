from django.shortcuts import render
from django_base import settings

from . import forms
# from part3.forms import FormName

def second(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Do Some Code
            print("VALIDATION SUCCES!")
            print("NAME: "+form.cleaned_data['name'])
            print("EMAIL: "+form.cleaned_data['email'])
            print("TEXT: "+form.cleaned_data['text'])

    return render(request,'part3/form.html',{"BASE_URL":settings.BASE_URL,'form':form})