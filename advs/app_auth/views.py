from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from app_advs.models import Advs

# Create your views here.
@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    advs = Advs.objects.filter(user=request.user)
    context = {'advs': advs}
    return render(request, 'auth/profile.html', context)

def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'auth/login.html', {'error' : 'пользователь не найден'})

def logout_view(request):
    logout(request)
    return redirect(reverse('login'))

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user=user)
            return redirect(reverse('profile'))
    else:
        form = CustomUserCreationForm()
    context = {'form': form}
    return render(request, 'auth/register.html', context)