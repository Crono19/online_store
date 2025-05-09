from django.urls import path
from . import views

urlpatterns = [
    path('', views.summary, name='summary'),
    path('add', views.add, name='add'),
    path('delete', views.delete, name='delete'),
    path('update', views.update, name='update'),
]
