from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import redirect
from django.db import IntegrityError
from .forms import SignUpForm
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from .forms import ForgotPasswordForm
from django.contrib.auth.forms import SetPasswordForm

# Create your views here.

def signupaccount(request):
    if request.method == 'GET':
        form = SignUpForm()
        return render(request, 'signupaccount.html', {'form': form})
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            try:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('dashboard')
            except IntegrityError:
                return render(request, 'signupaccount.html', {'form': form, 'error': 'Username already taken.'})
        else:
            return render(request, 'signupaccount.html', {'form': form})
        

def logoutaccount(request):
    logout(request)
    return redirect('loginaccount')

        
def loginaccount(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'loginaccount.html', {'error': 'Invalid email or password'})
    else:
        return render(request, 'loginaccount.html')
    

def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
                token = default_token_generator.make_token(user)
                reset_url = request.build_absolute_uri(reverse('reset_password', kwargs={'token': token}))

                # Send the reset password email
                send_mail(
                    'Password Reset Request',
                    f'You requested a password reset. Click the link below to reset your password:\n{reset_url}',
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )

                return render(request, 'forgot_password_success.html')
            except User.DoesNotExist:
                form.add_error('email', 'This email is not associated with any account.')
    else:
        form = ForgotPasswordForm()

    return render(request, 'forgot_password.html', {'form': form})

def reset_password(request, token):
    try:
        user = User.objects.get(id=default_token_generator.check_token(user, token))
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('loginaccount')
        else:
            form = SetPasswordForm(user)
    except:
        return redirect('forgot_password')

    return render(request, 'reset_password.html', {'form': form})

def forgot_password_success(request):
    return render(request, 'forgot_password_success.html')