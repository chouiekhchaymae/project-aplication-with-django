"""
URL configuration for projet1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from . import views
urlpatterns = [
    
    path('list_commande/',views.list_commande,name="list_commande"),
    path('ajout_commande/',views.ajoute_commande,name="ajout_commande"),
    path('modifier_commande/<str:pk>',views.modifier_commande,name="modifier_commande"),
    path('supprimer_commande/<str:pk>',views.supprimer_commande,name="supprimer_commande")


]
