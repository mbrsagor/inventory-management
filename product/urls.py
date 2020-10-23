from django.urls import path
from product.views.category_view import CategoryCreateView, CategoryListView

urlpatterns = [
    path('create-category/', CategoryCreateView.as_view(), name='create_category'),
    path('category-list/', CategoryListView.as_view(), name='category_list'),
]
