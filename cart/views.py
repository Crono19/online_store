from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .cart import Cart
from online_store.models import Product

def summary(request):
    cart = Cart(request)
    products = cart.view_cart()

    total = sum(item['total_price'] for item in products)
    quantities = cart.get_quantities()
    quantity_range = range(1, 11)

    return render(request, 'summary.html', {
        "products": products,
        "total": total,
        "quantities": quantities,
        "quantity_range": quantity_range,
    })

def add(request):
    cart = Cart(request)
    # Test for post
    if request.POST.get('action') == 'post':
        product_id = request.POST.get('product_id')
        product_quantity = request.POST.get('product_quantity')
        product = get_object_or_404(Product, id=product_id)
        
        # Save to session
        cart.add(product=product, quantity=product_quantity)
        
        # Get cart quantity
        cart_quantity = cart.__len__()
        
        return JsonResponse({'success': True, 'message': 'Producto añadido al carrito.', 'cart_quantity': cart_quantity})
    else:
        return JsonResponse({'success': False, 'message': 'Hubo un error al añadir el producto.'})

@require_POST
def update(request):
    product_id = request.POST.get('product_id')
    quantity = request.POST.get('quantity')

    try:
        product = Product.objects.get(id=product_id)
        cart = Cart(request)
        quantity = int(quantity)
        if quantity > 0:
            cart.cart[str(product.id)]['quantity'] = quantity
            cart.session.modified = True
    except (Product.DoesNotExist, ValueError, KeyError):
        pass  # silently fail or log

    return redirect('summary')  # or wherever your cart summary URL is

@require_POST
def delete(request):
    product_id = request.POST.get('product_id')

    try:
        cart = Cart(request)
        cart.remove_item(product_id)
    except KeyError:
        pass

    return redirect('summary')

