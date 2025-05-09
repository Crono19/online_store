from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Customer, Product, Order, UserProfile

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(UserProfile)

class ProfileInLine(admin.StackedInline):
    model = UserProfile

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["__all__"]
    inlines = [ProfileInLine]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)