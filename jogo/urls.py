from django.urls import path
from . import views 

urlpatterns=[
    path('', views.batalha, name='batalha'),
    path('teste/<int:id>', views.teste, name='teste'),
     
]