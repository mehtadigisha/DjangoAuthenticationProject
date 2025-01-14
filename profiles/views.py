from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

# Create your views here.

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'change_password.html', {'form': form})
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'change_password.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'dashboard.html', {'user': request.user})


@login_required
def profile(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        'date_joined': user.date_joined,
        'last_login': user.last_login,
    }
    return render(request, 'profile.html', context)