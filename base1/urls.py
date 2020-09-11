from django.urls import path
from . import views

app_name = 'base1'

urlpatterns = [
    path('',views.type,name='type'),
]