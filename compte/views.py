from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from compte.form import CreerUtilisateur
from django.contrib.auth.decorators import login_required

def inscriptionPage(request):
    form = CreerUtilisateur()
    if request.method == 'POST':
        form = CreerUtilisateur(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, "Compte créé avec succès pour " + user)
            return redirect('acces')
    context = {'form': form}
    return render(request, 'compte/inscreption.html', context)

def accesPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('acceuil')
        else:
            messages.info(request, "Il y a une erreur dans le nom d'utilisateur ou le mot de passe")
    context = {}
    return render(request, 'compte/acces.html', context)

@login_required(login_url='acces')
def acceuilPage(request):
    return render(request, 'produit/accuiel.html')

def logoutUser(request):
    logout(request)
    response = redirect('acces')
    response['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response['Pragma'] = 'no-cache'
    response['Expires'] = '0'
    return response
