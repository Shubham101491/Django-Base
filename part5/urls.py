from django.urls import path
from . import views

app_name = 'part5'

urlpatterns = [
    path('fifth/',views.fifth,name='fifth'),
    path('new/',views.new,name='new'),
    path('other/',views.other,name='other'),
]