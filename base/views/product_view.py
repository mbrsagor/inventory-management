from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.shortcuts import render, redirect, get_object_or_404

from base.models.product import Product
from base.models.category import Category
from base.forms.product_form import ProductForm
from base.addcart import Cart


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateProductView(SuccessMessageMixin, CreateView):
    template_name = 'product/add_product.html'
    model = Product
    form_class = ProductForm
    success_message = 'Product has been created'
    success_url = '/create-product/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class ProductListView(ListView):
    template_name = 'product/list_of_product.html'
    model = Product
    context_object_name = 'product'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryByProduct(ListView):
    template_name = 'product/category_by_product.html'
    model = Category
    context_object_name = 'category_by_product'


class ProductGridView(View):
    def get(self, request, id):
        product_filter = Product.objects.filter(product_category_id=id)
        context = {
            'product': product_filter
        }
        template_name = 'product/product_grid_view.html'
        return render(request, template_name, context)


# Add to cart views
def cart_add(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.add(product=product, quantity=1, update_quantity=1)
    return redirect('cart_detail')


# Remove Shopping Cart views
def cart_remove(request, id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=id)
    cart.remove(product)
    return redirect('cart_detail')


# Shopping Cart views
def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = {'quantity': item['quantity'], 'update': True}
    return render(request, 'product/cart.html', {'cart': cart})
