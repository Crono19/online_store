from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import (LoginForm)
from .models import Product, Category

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

def login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request, ("Sesión iniciada"))
                return redirect('home')
            else:
                messages.warning(request, ("Usuario o contraseña incorrectos. Inténtalo de nuevo."))
    
    messages.warning(request, ("Usuario o contraseña incorrectos. Inténtalo de nuevo."))
    return render(request, "login.html", {"form": form})

def logout(request):
    auth_logout(request)
    messages.success(request, ("Sesión cerrada"))
    return redirect('home')