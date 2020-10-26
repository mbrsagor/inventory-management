from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from product.models.category import Category
from product.models.inventory import Inventory


class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Dashboard, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['inventory'] = Inventory.objects.all()
        return context
