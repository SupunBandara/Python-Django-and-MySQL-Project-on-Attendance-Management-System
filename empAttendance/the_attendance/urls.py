from django.urls import path
from the_attendance import views

urlpatterns = [
    path('', views.attend_index, name='attend_index'),
  
    
    
]