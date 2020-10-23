from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from product.models.inventory import Inventory
from product.forms.inventory_form import InventoryForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateInventoryView(SuccessMessageMixin, CreateView):
    template_name = 'inventory/create_inventory.html'
    model = Inventory
    form_class = InventoryForm
    success_message = "Inventory successfully created!"
    success_url = '/config/create-inventory/'
