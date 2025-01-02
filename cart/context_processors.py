from .cart import Cart

# Return the cart content
def cart(request):
    return {'cart' : Cart(request)}