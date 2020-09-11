from django.urls import path
from . import views

app_name = 'part2'

urlpatterns = [
    path('first/',views.first,name='first'),
]