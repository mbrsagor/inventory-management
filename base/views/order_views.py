from base.models.order import OrderItem, Order
from django.shortcuts import render, redirect, get_object_or_404
from base.forms.order_form import OrderForm
from base.addcart import Cart


# Checkout views
def checkOutViews(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
    else:
        form = OrderForm()
    return render(request, 'pos/checkout.html', {'form': form, 'cart': cart})
