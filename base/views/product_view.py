from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from base.models.product import Product
from base.forms.product_form import ProductForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateProductView(SuccessMessageMixin, CreateView):
    template_name = 'product/add_product.html'
    model = Product
    form_class = ProductForm
    success_message = 'Product has been created'
    success_url = '/create-product/'
