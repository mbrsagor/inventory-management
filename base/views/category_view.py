from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from base.models.category import Category
from base.forms.category_form import CategoryForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryCreateView(SuccessMessageMixin, CreateView):
    template_name = 'category/create_category.html'
    success_message = "Category successfully created!"
    model = Category
    form_class = CategoryForm
    success_url = '/create-category/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryListView(ListView):
    template_name = 'category/category_list.html'
    model = Category
    context_object_name = 'category'
    paginate_by = 10


class CategoryUpdateView(UpdateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = '/category/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryDeleteView(DeleteView):
    template_name = 'category/category_confirm_delete.html'
    model = Category
    success_url = '/category/'
