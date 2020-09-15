from django.shortcuts import render,redirect
from django_base import settings

# Register Part
from partseven.forms import UserForm,UserProfileInfoForm
from django.contrib import auth

#Message   
from django.contrib import messages


def index(request):
    return render(request,'partseven/index.html')

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered =True
        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'partseven/registration.html',
                                    {'user_form':user_form,
                                    'profile_form':profile_form,
                                    'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        x = auth.authenticate(username=username,password=password)
        if x is None:
            return redirect('http://127.0.0.1:8000/partseven/user_login/')
        else:
            messages.info(request, 'Thankyou for contact us, we will reply you shortly')
            return redirect('http://127.0.0.1:8000/part3/second/')

    else:
        return render(request,'partseven/login.html',{"BASE_URL": settings.BASE_URL})

def user_logout(request):
    logout(request)
    messages.info(request,"Logged out successfully!")
    return redirect("http://127.0.0.1:8000/partseven/login/")