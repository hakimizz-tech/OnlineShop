from django.shortcuts import render

from cart.cart import Cart
from .forms import OrderForm
from .models import OrderItems
from .tasks import order_created


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItems.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'],
                )
            # clear the cart
            cart.clear()
            # launch asynchronous task
            order_created.delay(order.id)
            return render(
                request, 'orders/order/created.html', {'order': order}
            )
    else:
        form = OrderForm()
    return render(
        request,
        'orders/order/create.html',
        {'cart': cart, 'form': form},
    )
