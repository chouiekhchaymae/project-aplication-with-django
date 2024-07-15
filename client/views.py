from django.shortcuts import redirect, render,get_object_or_404
from commande.filter import CommandeFilter
# Create your views here.
from django.http import HttpResponse
from .models import Client
from client.form import ClientForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='acces')
def list_client(request,pk):
    client=Client.objects.get(id=pk)
    commande=client.commande_set.all()
    commande_total=commande.count()
    myFilter=CommandeFilter(request.GET,queryset=commande)
    commande=myFilter.qs
    context={'client':client,'commande':commande,'commande_total':commande_total,'myFilter':myFilter}
    return render(request,'client/list_client.html',context)

@login_required(login_url='acces')
# Afficher la liste des clients
def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client/clientList.html', {'clients': clients})

@login_required(login_url='acces')
# Ajouter un client
def ajoute_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'client/ajout_client.html', {'form': form})

@login_required(login_url='acces')
# Modifier un client
def modifier_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client/modifier_client.html', {'form': form})

@login_required(login_url='acces')
# Supprimer un client
def supprimer_client(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    if request.method == 'POST':
        client.delete()
        return redirect('client_list')
    return render(request, 'client/supprimer_client.html', {'client': client})