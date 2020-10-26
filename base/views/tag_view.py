from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin

from base.models.tag import Tag
from base.forms.tag_form import TagForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateListTagView(SuccessMessageMixin, CreateView, ListView):
    template_name = 'tag/tag_list.html'
    model = Tag
    form_class = TagForm
    success_message = "Category successfully created!"
    success_url = '/tag/'
    context_object_name = 'tag'
