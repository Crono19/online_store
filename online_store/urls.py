from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
    
    path('product/<int:pk>', views.product, name='product'),
    path('category/<str:name>', views.category, name='category'),
    path('search/', views.search_products, name='search'),
    path('ajax/search/', views.ajax_search, name='ajax_search'),
    path('ajax/search/category/<str:name>', views.ajax_search_category, name='ajax_search_category')
]
