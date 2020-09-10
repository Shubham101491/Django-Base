from django.urls import path
from . import views

urlpatterns = [
    path('forth/',views.forth,name='forth'),
]