from django.urls import path
from product.views.category_view import CategoryCreateView, CategoryListView, CategoryUpdateView, CategoryDeleteView

urlpatterns = [
    path('create-category/', CategoryCreateView.as_view(), name='create_category'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/<pk>/', CategoryUpdateView.as_view(), name='category_update'),
    path('category-delete/<pk>/', CategoryDeleteView.as_view(), name='category_delete'),
]
