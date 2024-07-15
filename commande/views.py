from django.shortcuts import redirect, render



# Create your views here.
from django.http import HttpResponse

from commande.form import CommandeForm
from commande.models import Commande
from django.contrib.auth.decorators import login_required

@login_required(login_url='acces')
def list_commande(request):
    commande = Commande.objects.all()
    return render(request,'commande/list_commande.html',{'commande': commande})

@login_required(login_url='acces')
def ajoute_commande(request):
    form=CommandeForm()
    if request.method=="POST":
        form=CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/ajoute_commande.html',context)

@login_required(login_url='acces')
def modifier_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    form=CommandeForm(instance=commande)

    if request.method=="POST":
        form=CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'commande/ajoute_commande.html',context)

@login_required(login_url='acces')
def supprimer_commande(request,pk):
    commande=Commande.objects.get(id=pk)
    if request.method=="POST":
        commande.delete()
        return redirect('/')
    context={'item':commande}
    return render(request,'commande/supprimer_comande.html',context)