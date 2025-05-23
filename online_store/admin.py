from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Customer, Product, Order, UserProfile
from cart.models import PersistentCart, PersistentCartItem

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserProfile)
admin.site.register(PersistentCart)
admin.site.register(PersistentCartItem)

class ProfileInLine(admin.StackedInline):
    model = UserProfile

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["__all__"]
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)