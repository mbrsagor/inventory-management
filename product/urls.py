from django.urls import path
from product.views.category_view import CategoryCreateView

urlpatterns = [
    path('create-category/', CategoryCreateView.as_view(), name='create_category'),
]
