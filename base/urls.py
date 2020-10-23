from django.urls import path
from base.views.dashboard_view import Dashboard
from base.views.auth_view import UserLoginView, LogoutView

urlpatterns = [
    path('', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
