from .cart import Cart

# Make the cart available in all templates
def cart(request):
    # Create a cart instance
    cart = Cart(request)
    return {'cart': cart}