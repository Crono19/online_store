from django.urls import path
from .views import (
    ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView,
    CategoryListView, CategoryCreateView, CategoryDetailView, CategoryUpdateView, CategoryDeleteView,
)

urlpatterns = [
    path('products/', ProductListView.as_view(),   name='product_list'),
    path('products/add/', ProductCreateView.as_view(), name='product_create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('products/<int:pk>/edit/', ProductUpdateView.as_view(), name='product_update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),

    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/add/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
