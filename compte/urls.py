from django.urls import path
from . import views

urlpatterns = [
    path('inscreption', views.inscriptionPage, name='inscreption'),
    path('acces', views.accesPage, name='acces'),
    path('quitter', views.logoutUser, name='quitter'),
    path('accuiel', views.acceuilPage, name='accuiel'),
]
