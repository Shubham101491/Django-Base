from django.urls import path
from . import views

app_name = 'part3'

urlpatterns = [
    path('second/',views.second,name='second'),
]