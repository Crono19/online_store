from online_store.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        # Check if the session has a cart
        cart = self.session.get("session_key")

        # If the cart does not exist, create a new one
        if 'session_key' not in self.session:
            # Create a new cart
            cart = self.session["session_key"] = {}
        
        # Make cart its available on all pages
        self.cart = cart

    def add(self, product, quantity=1):
        product_id = str(product.id)
        product_quantity = str(quantity)

        if product_id not in self.cart:
            self.cart[product_id] = {
                'name': product.name,
                'price': str(product.price),
                'quantity': int(product_quantity),
            }

        self.session.modified = True

    def view_cart(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        product_list = []

        for product in products:
            item = self.cart[str(product.id)]
            product_list.append({
                'product': product,
                'quantity': item['quantity'],
                'total_price': float(item['price']) * item['quantity']
            })

        return product_list

    def get_quantities(self):
        quantities = self.cart
        return quantities

    def remove_item(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True


    def __len__(self):
        return len(self.cart)
