from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.db import IntegrityError, transaction
from django.db.models import Q, F, Sum, FloatField
from django.contrib import messages
from django.core.exceptions import ValidationError
from online_store.models import (Product, Category)
from .forms import (ProductForm, CategoryForm)

# Product views
class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    queryset = Product.objects.filter(deleted=False)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'
    queryset = Product.objects.filter(deleted=False)

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            # add an error on the 'code' field:
            messages.warning(self.request, "Ya existe un producto con ese código.")
            return self.form_invalid(form)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_form.html'
    success_url = reverse_lazy('product_list')
    queryset = Product.objects.filter(deleted=False)

    def form_valid(self, form):
        try:
            return super().form_valid(form)
        except IntegrityError:
            # add an error on the 'code' field:
            messages.warning(self.request, "Ya existe un producto con ese código.")
            return self.form_invalid(form)
        
class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_confirm_delete.html'
    queryset = Product.objects.filter(deleted=False)
    success_url = reverse_lazy('product_list')

    def delete(self, request, *args, **kwargs):
        location = self.get_object()
        location.delete()
        messages.success(request, "Producto eliminado correctamente.")
        return super().post(request, *args, **kwargs)

# Category views
class CategoryListView(ListView):
    model = Category
    template_name = 'categories/category_list.html'
    context_object_name = 'categories'
    queryset = Category.objects.filter(deleted=False)

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'categories/category_detail.html'
    context_object_name = 'category'
    queryset = Category.objects.filter(deleted=False)

class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category_list')

    def form_valid(self, form):
        messages.success(self.request, "Categoría creada exitosamente.")
        return super().form_valid(form)
    
class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'categories/category_form.html'
    success_url = reverse_lazy('category_list')

    def get_queryset(self):
        return Category.objects.filter(deleted=False)

    def form_valid(self, form):
        messages.success(self.request, "Categoría actualizada exitosamente.")
        return super().form_valid(form)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'categories/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

    def get_queryset(self):
        return Category.objects.filter(deleted=False)

    def delete(self, request, *args, **kwargs):
        category = self.get_object()
        category.delete()  # usa el método que marca como deleted=True
        messages.success(request, "Categoría eliminada exitosamente.")
        return super().post(request, *args, **kwargs)
