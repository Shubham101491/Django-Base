from django.urls import path
from . import views

app_name = 'parteight'

urlpatterns = [
    path('crud/',views.crud,name='crud'),
    path('show/',views.show,name='show'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update'),
    path('delete/<int:id>',views.delete,name='delete'),
    
]