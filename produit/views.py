from django.shortcuts import render
from commande.filter import CommandeFilter
from produit.models import Produit
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.
from django.http import HttpResponse
from commande.models import Commande
from client.models import Client
from django.contrib.auth.decorators import login_required
from produit.form import ProductForm

@login_required(login_url='acces')
def home(request):
    commandes= Commande.objects.all()
    clients=Client.objects.all()
    context={'commandes':commandes,'clients':clients}
    return render(request,'produit/accuiel.html',context)

# Liste des produits
def product_list(request):
    products = Produit.objects.all()
    return render(request, 'produit/listProduit.html', {'products': products})

# Ajouter un produit
def product_add(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'produit/product_form.html', {'form': form})

# Modifier un produit
def product_edit(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'produit/product_form.html', {'form': form})

# Supprimer un produit
def product_delete(request, pk):
    product = get_object_or_404(Produit, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'produit/product_confirm_delete.html', {'product': product})