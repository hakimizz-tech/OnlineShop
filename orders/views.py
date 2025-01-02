from django.shortcuts import render

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItems


# Create your views here.


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()  #creating an instance of the Order
            for item in cart:  #iterate the items in the cart and create an OrderItem for each cart
                OrderItems.objects.create(
                    order = order,
                    product = item['product'],
                    price = item['price'],
                    quantity = item['quantity'],
                )
            # clear the cart
            cart.clear()
            return render(request, 'orders/order/created.html', {'order' : order} )
    else:
        form = OrderForm()

    return render(request, 'orders/order/create.html', {'cart' : cart, 'form': form} )