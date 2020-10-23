from django.views.generic import CreateView, ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.messages.views import SuccessMessageMixin

from product.models.category import Category
from product.forms.category_form import CategoryForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = 'category/create_category.html'
    success_message = "Category successfully created!"
    model = Category
    form_class = CategoryForm
    success_url = '/config/create-category/'


class CategoryListView(ListView):
    template_name = 'category/category_list.html'
    model = Category
    context_object_name = 'category'
    paginate_by = 10
