from django.urls import path
from . import views

app_name = 'partseven'

urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('index/',views.index,name='index'),
]