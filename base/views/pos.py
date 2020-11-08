from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from base.models.product import Product
from base.addcart import Cart


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class POSView(TemplateView):
    template_name = 'pos/pos.html'

    def get_context_data(self, **kwargs):
        context = super(POSView, self).get_context_data(**kwargs)
        context['cosmetic'] = Product.objects.filter(product_category__id=1)
        context['tech'] = Product.objects.filter(product_category__id=3)
        context['laptop'] = Product.objects.filter(product_category__id=4)
        context['food'] = Product.objects.filter(product_category__id=6)
        return context


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


# Shopping Cart views
def bulling_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = {'quantity': item['quantity'], 'update': True}
    template_name = 'pos/bulling.html'
    return render(request, template_name, {'cart': cart})


@require_POST
def cart_updated(request, id):
    cart = Cart(request)
    if request.method == 'POST':
        number = int(request.POST.get('number'))
    product = get_object_or_404(Product, id=id)
    cart.add(product=product, quantity=number, update_quantity=True)
    return redirect('pos_view')
