from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .forms import (LoginForm, CustomUserCreationForm)
from .models import Product, Category

# Create your views here.
def home(request):
    products = Product.objects.filter(deleted=False)
    return render(request, 'home.html', {'products': products})

def about(request):
    return render(request, 'about.html', {})

from django.contrib.auth.models import Group

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                preserved_cart = request.session.get("session_key", {}).copy()

                auth_login(request, user)

                request.session["session_key"] = preserved_cart
                request.session.modified = True

                messages.success(request, "Sesión iniciada")

                # Verificar grupo y redirigir
                if user.groups.filter(name="Administrador").exists():
                    return redirect('product_list')
                else:
                    return redirect('home')

        messages.warning(request, "Usuario o contraseña incorrectos. Inténtalo de nuevo.")

    return render(request, "login.html", {"form": form})

def logout(request):
    preserved_cart = request.session.get("session_key", {}).copy()

    auth_logout(request)

    request.session["session_key"] = preserved_cart
    request.session.modified = True

    messages.success(request, "Sesión cerrada")
    return redirect('home')


def product(request, pk):
    product = Product.objects.get(pk=pk)
    quantity_range = range(1, 11)
    
    previous_page = request.META.get('HTTP_REFERER', reverse('home'))  # fallback to home

    return render(request, 'product.html', {
        'product': product,
        'quantity_range': quantity_range,
        'previous_page': previous_page
    })


def category(request, name):
    name = name.replace("-", " ")
    category = get_object_or_404(Category, name__iexact=name, deleted=False)
    products = Product.objects.filter(category=category)
    return render(request, 'category.html', {'category': category, 'products': products})

def search_products(request):
    query = request.GET.get('q')
    products = Product.objects.filter(name__icontains=query) if query else []
    return render(request, 'search_results.html', {'products': products, 'query': query})

def ajax_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(name__icontains=query, deleted=False) if query else Product.objects.filter(deleted=False)
    html = render_to_string('partials/_product_list.html', {'products': products})
    return JsonResponse({'html': html})

def ajax_search_category(request, name):
    query = request.GET.get('q', '')
    category = get_object_or_404(Category, name__iexact=name, deleted=False)
    products = Product.objects.filter(name__icontains=query, category=category, deleted=False)[:10] if query else Product.objects.filter(category=category, deleted=False)
    html = render_to_string('partials/_product_list_category.html', {'products': products})
    return JsonResponse({'html': html})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cuenta creada correctamente. Ya puedes iniciar sesión.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})