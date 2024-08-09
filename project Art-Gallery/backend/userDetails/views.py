from django.shortcuts import render, redirect
from django.urls import reverse
# Create your views here.
from django.contrib.auth import login
from .forms import CustomUserCreationForm, CustomAuthenticationForm

def Signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse('home'))  # Redirect to a home page or dashboard
    else:
        form = CustomUserCreationForm()
    return render(request, 'Signup.html', {'form': form})

def Signin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect(reverse('home'))  # Redirect to a home page or dashboard
    else:
        form = CustomAuthenticationForm()
    return render(request, 'Signin.html', {'form': form})
