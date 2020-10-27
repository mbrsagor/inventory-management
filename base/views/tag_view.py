from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from base.models.tag import Tag
from base.forms.tag_form import TagForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CreateListTagView(SuccessMessageMixin, CreateView, ListView):
    template_name = 'tag/tag_list.html'
    model = Tag
    form_class = TagForm
    success_message = "Tag has been successfully created!"
    success_url = '/tag/'
    context_object_name = 'tag'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(CreateListTagView, self).get_context_data(**kwargs)
        tag = self.get_queryset()
        page = self.request.GET.get('page')
        paginator = Paginator(tag, self.paginate_by)

        try:
            tag = paginator.page(page)
        except PageNotAnInteger:
            tag = paginator.page(1)
        except EmptyPage:
            tag = paginator.page(paginator.num_pages)
        context['tag'] = tag
        return context


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class UpdateTagView(UpdateView):
    template_name = 'tag/tag_list.html'
    model = Tag
    form_class = TagForm
    success_url = '/tag/'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TagDeleteView(DeleteView):
    template_name = 'tag/tag_confirm_delete.html'
    model = Tag
    success_url = '/tag/'
