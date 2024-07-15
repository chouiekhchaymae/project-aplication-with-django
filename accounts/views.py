from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login

def password_reset_request(request):
    if request.method == "POST":
        username = request.POST.get("username")
        try:
            user = User.objects.get(username=username)
            request.session['reset_user_id'] = user.id
            return redirect('password_reset_confirm')
        except User.DoesNotExist:
            return render(request, 'accounts/password_reset.html', {'error': 'Utilisateur non trouvé'})
    return render(request, 'accounts/password_reset.html')

def password_reset_confirm(request):
    if request.method == "POST":
        new_password = request.POST.get("new_password")
        user_id = request.session.get('reset_user_id')
        if not user_id:
            return redirect('password_reset')
        try:
            user = User.objects.get(id=user_id)
            user.set_password(new_password)
            user.save()
            return redirect('password_reset_complete')
        except User.DoesNotExist:
            return render(request, 'accounts/password_reset_confirm.html', {'error': 'Erreur utilisateur'})
    return render(request, 'accounts/password_reset_confirm.html')

def password_reset_done(request):
    return render(request, 'accounts/password_reset_done.html')

def password_reset_complete(request):
    return render(request, 'accounts/password_reset_complete.html')
