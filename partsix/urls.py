from django.urls import path
from . import views

app_name = 'partsix'

urlpatterns = [
    path('new/',views.new,name='new'),
    path('other/',views.other,name='other'),
]