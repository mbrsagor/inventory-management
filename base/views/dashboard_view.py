from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User

from base.models.category import Category
from base.models.tag import Tag
from base.models.inventory import Inventory


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class Dashboard(TemplateView):
    template_name = 'dashboard/dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Dashboard, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        context['inventory'] = Inventory.objects.all()
        context['user'] = User.objects.all()
        context['tag'] = Tag.objects.all()
        return context
