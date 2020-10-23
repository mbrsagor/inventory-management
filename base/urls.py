from django.urls import path
from base.views.dashboard import Dashboard

urlpatterns = [
    path('', Dashboard.as_view(), name='dashboard'),
]
