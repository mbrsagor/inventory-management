from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.shortcuts import render

from base.models.product import Product
from base.models.category import Category
from base.forms.product_form import ProductForm


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

