from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from base.models.product import Product
from base.addcart import Cart


class POSView(View):

    def get(self, request):
        cosmetic = Product.objects.filter(product_category__id=1)
        tech = Product.objects.filter(product_category__id=3)
        laptop = Product.objects.filter(product_category__id=4)
        food = Product.objects.filter(product_category__id=6)
        cart = Cart(request)

        for item in cart:
            item['update_quantity_form'] = {'quantity': item['quantity'], 'update': True}

        context = {
            'cosmetic': cosmetic,
            'tech': tech,
            'laptop': laptop,
            'food': food,
            'cart': cart
        }
        template_name = 'pos/pos.html'
        return render(request, template_name, context)


# Add to cart views
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product, quantity=1, update_quantity=1)
    return redirect('pos_view')


# Remove Shopping Cart views
def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('pos_view')


# update Shopping Cart views
@require_POST
def cart_updated(request, id):
    number = None
    cart = Cart(request)
    if request.method == 'POST':
        number = int(request.POST.get('number'))
    product = get_object_or_404(Product, id=id)
    cart.add(product=product, quantity=number, update_quantity=True)
    return redirect('pos_view')
