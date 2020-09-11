from django.urls import path
from . import views

app_name = 'part4'

urlpatterns = [
    path('forth/',views.forth,name='forth'),
]