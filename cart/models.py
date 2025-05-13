from django.contrib.auth.models import User
from django.db import models
from online_store.models import Product

class PersistentCart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')

    def __str__(self):
        return f"Carrito de {self.user.username}"

class PersistentCartItem(models.Model):
    cart = models.ForeignKey(PersistentCart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
