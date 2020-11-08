from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from base.models.product import Product


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class POSView(TemplateView):
    template_name = 'product/pos.html'

    def get_context_data(self, **kwargs):
        context = super(POSView, self).get_context_data(**kwargs)
        context['cosmetic'] = Product.objects.filter(product_category__id=1)
        context['tech'] = Product.objects.filter(product_category__id=3)
        context['laptop'] = Product.objects.filter(product_category__id=4)
        context['food'] = Product.objects.filter(product_category__id=6)
        return context
