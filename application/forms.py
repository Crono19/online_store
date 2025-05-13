from django import forms
from django.forms import inlineformset_factory, BaseInlineFormSet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from online_store.models import (Product, Category)

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('deleted',)
        fields = '__all__' 

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ('deleted',)
        fields = '__all__' 