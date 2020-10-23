from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout
from django.shortcuts import resolve_url
from django.views import View
from django.shortcuts import redirect

from base.forms.login_form import LoginForm


# User login view
class UserLoginView(LoginView):
    authentication_form = LoginForm
    form_class = LoginForm
    redirect_authenticated_user = False
    template_name = 'auth/login.html'

    def get_success_url(self):
        url = self.get_redirect_url()
        return url or resolve_url('/dashboard/')

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        login(self.request, form.get_user())

        if remember_me:
            self.request.session.set_expiry(1209600)
        return super(UserLoginView, self).form_valid(form)


# Logout view
class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')
