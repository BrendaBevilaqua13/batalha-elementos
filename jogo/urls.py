from django.urls import path
from . import views

urlpatterns=[
    path('', views.baralho, name='baralho'),
     
]